# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji, KnownKanji, KnownWords, UserSets
from django.db.models import Count, Min, Sum, Avg
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from django.utils.timezone import utc
import time
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from api.serializers import * 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes 
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from utils import * 

def index(request):
    return render(request,'production-dist/index.html')
    
@api_view(['GET'])
def get_master_review_decks(request):
    decks = Sets.objects.exclude(master_order__isnull=True)
    serializer = SetsSerializerWithoutWords(decks, many=True)
    data = serializer.data
    return Response(data)

@api_view(['GET'])
def get_user_sets(request):
    userprofile = request.user.userprofile
    decks = UserSets.objects.filter(user_profile_fk = userprofile).order_by('id')
    serializer = UserSetsSerializer(decks, many=True)
    data = serializer.data

    chunked_data = [] 
    size = 20;
    deckArrayLength = len(data)
    chunk = { 'chunk_list': [] }

    completed_count = 0
    for index, each in enumerate(data):
        if each['completion_status']: completed_count += 1
        chunk['chunk_list'].append(data[index])
        if (index + 1) % size == 0 or index == deckArrayLength - 1:
            chunk['completed_count'] = completed_count 
            chunked_data.append(chunk)
            completed_count = 0
            chunk = { 'chunk_list': [], 'complete_count': 0 }

    return Response(chunked_data)

@api_view(['GET'])
def get_analytics_data(request):
    username = request.user.username
    todays_log = AnalyticsLog.objects.get_or_create(request.user)
    serializer = AnalyticsLogSerializer(todays_log)
    data = serializer.data
    return Response(data)

@api_view(['GET'])
def get_chart_data(request):
    userprofile = request.user.userprofile
    analytics_logs = AnalyticsLog.objects.filter(user_profile = userprofile)
    log_count = analytics_logs.count()
    #TODO for future -  split different chart queries into different functions or a switch statement
    words_studied_count = list(analytics_logs.values_list('words_studied_count', flat=True).order_by('last_modified'))
    words_studied_count.insert(0, 0)
    master_words_count = Words.objects.filter(master_order__gt=0).count()

    base = date.today()
    date_list = [base - timedelta(days=x) for x in range(log_count, -1, -1)]
    ideal_data_points = [ 15 * x for x in range(0, log_count + 1)]
    return Response({'x_axis_data':date_list,
                    'data_points':words_studied_count,
                    'ideal_data_points':ideal_data_points})

# TODO look into moving each individual calculation into model
@api_view(['GET'])
def get_review_data(request):
    userprofile = request.user.userprofile
    update_word_queue(request.user)
    known_words = KnownWords.objects.filter(user_profile = userprofile)

    tier_counts = known_words.values('tier_level').annotate(count = Count('tier_level')).order_by('tier_level')
    master_word_count = Words.objects.filter(master_order__gt=0).count()
    count_dict = {}
    studied_word_sum = 0
    for each in tier_counts:
        count_dict[each['tier_level']] = each['count']
    #if not in above count_dict then set to 0
    for each in range(10):
        try:
            studied_word_sum += count_dict[each]
        except KeyError:
            count_dict[each] = 0
    count_dict[0] = master_word_count - studied_word_sum

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
        next_review = str(timedelta(seconds = next_review_time['time_until_review'])).split('.')[0]
    else:
        next_review = reviews_due_count 
    
    return JsonResponse({'next_review':next_review, 'next_day':reviews_24_hours_count, 'tier_counts':count_dict, 'username':request.user.username })
