from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji, KnownWords
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
import json
import random
from datetime import datetime, timedelta, time
from django.core.context_processors import csrf
# import pytz
from django.utils.timezone import utc
from django.db.models import F


# Create your views here.
def practice_stack(request, full_name, set_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
        return HttpResponse("you are not authenticated")
    else: 
        userprofiles = User.objects.get(username = full_name).userprofile.id
        userprofile = get_object_or_404(UserProfile, pk = userprofiles)
        words = Sets.objects.get(name = set_name, userprofile = userprofiles).words.all() 
        return render(request, 'flashcard/practicecards.html', {'full_name':full_name, 'words':words, 'set_name': set_name})
        

def complete_stack(request, full_name, set_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
        return HttpResponse("you are not authenticated")
    else:
        if request.is_ajax():
            try:
                
                theset = request.GET['set_name']
                the_set_object = Sets.objects.get(name = theset)
                if the_set_object.times_practiced == 0:
                    
                    the_set_object.times_practiced = 1
                    
                    userprofiles = User.objects.get(username = full_name).userprofile.id
                    words = request.GET['wordlist']
                    
                    
                    # data = serializers.serialize("json",words)
                    data = json.loads(words)
                    
                    
                    words_practiced = []
                    
                    for each in data:  
                        print each
                        # this is really confusing (this is actually the id of the word, not the KnownWord Object), temporary fix so that practicecard template will work for both reviews and stacks
                        words_practiced.append(each['know_word_object_id'])
                        
                        
                        
                    KnownWords.objects.filter(user_profile = userprofiles, words__in = words_practiced).update(last_practiced = datetime.now(), tier_level = 1, time_until_review = timedelta(hours = 5).total_seconds())
                    
                    the_set_object.save()
                    data = json.dumps(words)
                    
                    
                else:
                    data = 1    
                
            except KeyError:
                return HttpResponse("there was an error")
        return HttpResponse(data, content_type="application/json")
        
        

def srs_review_words(request, full_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
        return HttpResponse("you are not authenticated")
    else:
        
            words_list = srs_get_and_update(request, full_name)
               
    return render(request, 'flashcard/review-cards.html', {'full_name':full_name, 'words':words_list})
    

def srs_get_and_update(request, full_name):
    
    # words = [2,3,4,5]
    userprofiles = User.objects.get(username = full_name).userprofile.id
    userprofile = get_object_or_404(UserProfile, pk = userprofiles)
    # words = Sets.objects.get(name = "Drew", userprofile = userprofiles).words.all()
    words = KnownWords.objects.filter(user_profile = userprofiles, tier_level__lte = 9).exclude(tier_level = 0).exclude(time_until_review = None).order_by('time_until_review')
    words_list = []
    known_word_id = []
    
    for word in words:
        last_practiced = word.last_practiced
        now = datetime.utcnow().replace(tzinfo=utc)
        difference = now - last_practiced
        difference = difference.total_seconds()
        
        time_remaining = word.time_until_review - difference
        
        # print "now: ", now
 #        print "last practiced ", last_practiced
 #        print "difference: ", difference
 #        print "time remaining: ", time_remaining
 #        print "tier level: ", word.tier_level
        word.time_until_review = time_remaining
        word.last_practiced = now
        word.save()
        if time_remaining <= 0:
            word.words.id = word.id
            words_list.append(word.words)
            
            
            
    
    return words_list 



def tier_level_update(request, full_name):
  
    if not request.user.is_authenticated() or request.user.username != full_name:
        return HttpResponse("you are not authenticated")
    else:
        if request.is_ajax():
            try:

                userprofiles = User.objects.get(username = full_name).userprofile.id
                known_id = request.GET['known_object_id']
                increase_level = int(request.GET['increase_level'])
                
                options = {     0 : 0,
                                1 : 4,
                                2 : 22,
                                3 : 75,
                                4 : 185,
                                5 : 450,
                                6 : 1050,
                                7 : 2500,
                                8 : 6200,
                                9 : 15000
                }
                
                selected_word = KnownWords.objects.get(id = known_id)
                selected_word_tier = KnownWords.objects.get(id = known_id).tier_level
                selected_word.last_practiced = datetime.now()
                
                print "this is the increase level flag :", type(increase_level), increase_level  
                print "original level: ", selected_word_tier
                if increase_level == 1:
                    print "hello" 
                    if selected_word_tier <10:
                        selected_word.tier_level = selected_word_tier + 1
                        
                elif selected_word_tier != 1:
                    selected_word.tier_level = selected_word_tier - 1
                    
                            
                
                new_hours = options[selected_word.tier_level]
                
                random_multiplier = random.uniform(.90, 1.10)
                
                selected_word.time_until_review = timedelta(hours = new_hours).total_seconds() * random_multiplier
                
                print "this is the new level: ", selected_word.tier_level
                print selected_word.time_until_review, "this is the time added"
                
                selected_word.save()
                
                data = 1

            except KeyError:
                return HttpResponse("there was an error")
            return HttpResponse(data, content_type="application/json")




    
    


            