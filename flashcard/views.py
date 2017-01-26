from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji, KnownWords, UserSets
from manageset.utils import * 
from django.contrib.auth.models import User
from django.core import serializers
from datetime import datetime, timedelta, time
from django.utils.timezone import utc
from django.views.decorators.cache import cache_control
from django.http import JsonResponse
from api.serializers import SetsSerializer, KnownWordsSerializer
import json
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes 
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework import status
        
@api_view(['GET'])
def get_review_deck(request, level, sub_level):
    deck = Sets.objects.filter(level=level, sub_level=sub_level)
    serializer = SetsSerializer(deck, many=True)
    data = serializer.data
    return Response(data)

@api_view(['POST'])
def review_deck_complete(request):
    data = json.loads(request.body)
    profile = request.user.userprofile
    stack_id = data.get('stack_id') 
    user_set = UserSets.objects.get(sets_fk = stack_id, user_profile_fk = profile)
    if not user_set.completion_status:
        user_set.completion_status = True
        user_set.save()
        deck = Sets.objects.get(id = stack_id)
        words = deck.words.all()
        words_to_add = []
        for word in words:
            new_word = KnownWords(words = word, user_profile = profile)
            new_word.set_initial_level()
            words_to_add.append(new_word)
        KnownWords.objects.bulk_create(words_to_add)
    return Response(status=status.HTTP_200_OK)

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
