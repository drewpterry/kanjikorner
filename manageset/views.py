# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji, KnownKanji, KnownWords
from django.db.models import Count, Min, Sum, Avg
from django.contrib.auth.models import User
from django.db.models import Q
from django.core import serializers
from datetime import datetime, timedelta, date
from django.utils.timezone import utc
import time
from django.utils import timezone
from django.template.context_processors import csrf
from collections import deque
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_control
from django.views.generic import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
import re
from django.http import JsonResponse
from api.serializers import * 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes 
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from utils import update_word_queue 


def verify_profiles(request,full_name):
    return
    # if not request.user.is_authenticated() or request.user.username != full_name:
        # return False
            
not_auth = HttpResponse("you are not authenticated")

@login_required
def view_dashboard(request):
    return render(request,'dist/index.html')
    
@api_view(['GET'])
def get_master_review_decks(request):
    decks = Sets.objects.exclude(master_order__isnull=True)
    serializer = SetsSerializerWithoutWords(decks, many=True)
    data = serializer.data
    return Response(data)

@api_view(['GET'])
def get_profile_data(request):
    userprofile = request.user.userprofile
    serializer = UserProfileSerializer(userprofile)
    data = serializer.data
    return Response(data)

@api_view(['GET'])
def get_review_data(request):
    userprofile = request.user.userprofile
    update_word_queue(request.user)
    known_words = KnownWords.objects.filter(user_profile = userprofile)
    reviews_due_count = known_words.filter(time_until_review__lte = 0).count()
    reviews_24_hours = (known_words.filter(
        user_profile = userprofile,
        #within the next day
        time_until_review__range = (0,86400))
        .values('time_until_review')
        .order_by('time_until_review')
        )
    next_review_time = reviews_24_hours.first()
    reviews_24_hours_count = reviews_24_hours.count() + reviews_due_count 
    if reviews_due_count == 0 and next_review_time:
        next_review = str(timedelta(seconds = next_review_time)).split('.')[0]
    else:
        next_review = reviews_due_count 
    
    return JsonResponse({'next_review':next_review, 'next_day':reviews_24_hours_count})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required 
def main_profile(request,full_name):
    if verify_profiles(request,full_name) == False:
            return not_auth
    else:
        
        userprofile = UserProfile.objects.get(user = request.user)
        #delete once finished
        usersets = userprofile.user_sets.all().order_by('pub_date').prefetch_related('words')
        # decks = Sets.objects.exclude(master_order = None).order_by('master_order')
        
        user_known_words = KnownWords.objects.filter(user_profile = userprofile)
        known_words = user_known_words.values('tier_level').annotate(count = Count('tier_level')).order_by('tier_level')
        total_word_count = user_known_words.exclude(tier_level__in = [0,10]).count()
        one_day_ago = datetime.now() - timedelta(days = 1)
        words_reviewed_today = userprofile.number_words_practiced_today
        words_reviewed_today_best = userprofile.most_words_practiced_in_day
        
        total_review_right = user_known_words.aggregate(Sum('times_answered_correct'))
        total_review_wrong = user_known_words.aggregate(Sum('times_answered_wrong'))
        try:
            total_reviews_ever = total_review_wrong['times_answered_wrong__sum'] + total_review_right['times_answered_correct__sum']
        except:
           total_reviews_ever = 0     
        
        count_dict = {}
        
        for each in known_words:
            count_dict[each['tier_level']] = each['count']
            
        for each in range(10):
            try:
                count_dict[each]
            except KeyError:
                count_dict[each] = 0
                
        number_of_added_kanji =  KnownKanji.objects.filter(user_profile = userprofile).count()
        number_of_reviews = len(srs_get_and_update(request, full_name))
        next_review = KnownWords.objects.filter(user_profile = userprofile, time_until_review__range = (0,86400)).values('time_until_review').order_by('time_until_review')
        due_tomorrow = len(next_review) + number_of_reviews
        kanji_percent = round(number_of_added_kanji /21.36, 2) 
        if number_of_reviews == 0:
            if next_review.exists():
                next_review = next_review[0]
                next_review = next_review['time_until_review']
                next_review = str(timedelta(seconds = next_review)).split('.')[0]
        else:
            next_review = "Now"
            
        
        return render(request,'manageset/dashboard_new.html', {'full_name':full_name, 'usersets': usersets, 'review_number': number_of_reviews, \
         'the_count':count_dict, 'next_review':next_review, 'due_tomorrow':due_tomorrow, 'added_kanji_count': number_of_added_kanji,\
          'word_count':total_word_count, 'words_reviewed_today':words_reviewed_today, 'total_reviews_ever':total_reviews_ever, 'kanji_percent':kanji_percent,"words_reviewed_today_best":words_reviewed_today_best})
