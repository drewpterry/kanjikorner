from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji, KnownWords
from manageset.utils import * 
from django.contrib.auth.models import User
from django.core import serializers
import json
import random
from datetime import datetime, timedelta, time
from django.template.context_processors import csrf
from django.utils.timezone import utc
from django.db.models import F
from django.views.decorators.cache import cache_control
from forms import WordMeaningUpdate
from django.http import JsonResponse
from api.serializers import SetsSerializer, KnownWordsSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes 
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
        
@api_view(['GET'])
def get_review_deck(request, level, sub_level):
    deck = Sets.objects.filter(level=level, sub_level=sub_level)
    serializer = SetsSerializer(deck, many=True)
    data = serializer.data
    return Response(data)

def view_review_deck(request, level, sub_level):
    return render(request, 'flashcard/practicecards.html')

@api_view(['GET'])
def get_srs_review(request):
    profile = request.user.userprofile
    update_word_queue(request.user)
    words = (KnownWords.objects.filter(
        user_profile = profile,
        tier_level__lte = 7,
        time_until_review__lte = 0)
        .exclude(tier_level = 0).
        exclude(time_until_review = None).
        order_by('time_until_review')
        )
    serializer = KnownWordsSerializer(words, many=True)
    data = serializer.data
    return Response(data)

def view_srs_review(request):
    return render(request, 'flashcard/practicecards.html')

@api_view(['POST'])
def update_review_word(request):
    data = json.loads(request.body)
    profile = request.user.userprofile
    # timezone_adjustment = int(request.GET['timezone_offset'])
    known_word_id = data.get('known_word_id') 
    increase_level = int(data.get('increase_level'))
    #TODO this probably shouldn't accept knownID, it will probably find word based off of Word assocation
    selected_word = KnownWords.objects.get(id = known_word_id, user_profile = profile)
    selected_word.update_tier_and_review_time(increase_level)
    selected_word.save()
    # profile.update_words_practiced_today(timezone_adjustment)
    # profile.save()
    data = 1
    return Response(data)
