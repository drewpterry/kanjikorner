# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Q
import json
from django.utils import simplejson
from django.core import serializers
from datetime import datetime
from django.core.context_processors import csrf
# import pdb; pdb.set_trace()

# Create your views here.

def verify_profiles(request,full_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
            # return render(request, 'myapp/login_error.html')
            return False
            
not_auth = HttpResponse("you are not authenticated")

def main_profile(request,full_name):
    if verify_profiles(request,full_name) == False:
            return not_auth
    else:
        userprofiles = User.objects.get(username = full_name).userprofile.id
        userprofile = get_object_or_404(UserProfile, pk = userprofiles)
        return render(request,'manageset/profile.html', {'full_name':full_name, 'usersets':userprofile})
        
        
def create_new_set(request,full_name):
    if verify_profiles(request,full_name) == False:
            return not_auth
    else:
        kanjis = Kanji.objects.all()
        return render(request, "manageset/create-set.html", {'full_name':full_name, 'kanjis':kanjis})   
        

def word_search(request):
    #for some reason this doesnt work when i pass in full_name
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                ordering = request.GET['theorder']
                searchword = request.GET['searchword']
                kanji = Kanji.objects.filter(kanji_meaning__contains = searchword).order_by(ordering, 'grade', 'id')[0:200]
                data = serializers.serialize("json",kanji)
            except KeyError:
                return HttpResponse("error")    
        # dump = simplejson.dumps(kanji)   
        return HttpResponse(simplejson.dumps(data), content_type="application/json")   
        # return HttpResponse("hello")
        
        
def add_words_to_set(request,full_name):
    c = {}
    c.update(csrf(request))
    userprofiles = User.objects.get(username = full_name).userprofile.id
    userprofile = get_object_or_404(UserProfile, pk = userprofiles)
    setname = request.POST['title']
    description = request.POST['description']
    
    chosenwords = request.POST.getlist('chosenwords')
    thechosenwords = []
    
    for words in chosenwords:
        obj1 = Words.objects.get(id = words)
        thechosenwords.append(obj1)
        
    newset = Sets(name = setname, description = description, pub_date = datetime.now())
    newset.save()
    newset.words.add(*thechosenwords)
    userprofile.user_sets.add(newset)
    return render(request, "manageset/create-set-confirm.html", {'setname':setname, 'chosenwords':thechosenwords})
    
def add_known_words(request, full_name):    
    c = {}
    c.update(csrf(request))
    userprofiles = User.objects.get(username = full_name).userprofile.id
    userprofile = get_object_or_404(UserProfile, pk = userprofiles)
    knownkanji = request.POST.getlist('known-kanji')
    theknownkanji = []
    
    for kanji in knownkanji:
        if UserProfile.objects.get(id = userprofiles).known_kanji.filter(id = kanji).exists() == False:
            obj1 = Kanji.objects.get(id = kanji)
            theknownkanji.append(obj1)
            
    
    userprofile.known_kanji.add(*theknownkanji)    
    #submit known words
    return render(request,"manageset/known-words-page.html", {'full_name': full_name, 'knownkanji': theknownkanji})
    # return
   
    
def view_known_words(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                # ordering = request.GET['theorder']
                # searchword = request.GET['searchword']
               
                profile = request.user.userprofile
                profile_known_kanji = profile.known_kanji.all()
                
                kanji_in = []
                for each in profile_known_kanji:
                    kanji_in.append(each.id)
                
                print kanji_in
                
                i = 1
                kanji_list = []
                while i < 2417:
                    if i not in kanji_in:
                        kanji_list.append(i)
                    i = i + 1
                
                words = Words.objects.filter(kanji__in = kanji_in).exclude(frequency = 0).order_by('frequency','pk').distinct()[0:1400]
                
                # cursor =  connection.cursor()
  #               sql = '''SELECT p.id, real_word, k.words_id
  # FROM manageset_words p
  # LEFT
  # JOIN ( SELECT j.kanji_id, j.words_id
  #          FROM manageset_words_kanji j
  #         WHERE j.kanji_id IN ('287')
  #      ) k
  #   ON k.words_id = p.id
  # WHERE k.words_id IS NOT NULL'''
  #
  #
  #               cursor.execute(sql)
#                 row = cursor.fetchall()
                data = serializers.serialize("json",words)
                data = json.loads(data)
                
                for each in list(data):
                    thelist = list(set(each[u'fields'][u'kanji'])-set(kanji_in))
                    if thelist:
                        data.remove(each)
                        
                data = data[:50]
                data = json.dumps(data)
                
                     
            except KeyError:
                return HttpResponse("there was an error")       
        return HttpResponse(data, content_type="application/json")
         
    
    
def view_stack(request,full_name, set_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
            return HttpResponse("you are not authenticated")
    else:
        userprofiles = User.objects.get(username = full_name).userprofile.id
        userprofile = get_object_or_404(UserProfile, pk = userprofiles)
        return render(request, "manageset/view_set.html", {'full_name':full_name, 'set_name':set_name})
           
                
def view_stack_search(request):
    if not request.user.is_authenticated():
        return HttpResponse("you are not authenticated")
    else:
        if request.is_ajax():
            try:
                fullname = request.POST['full_name']
                setname = request.POST['set_name']
                userprofiles = User.objects.get(username = fullname).userprofile.id
                ordering = request.POST['theorder']
                userprofile = get_object_or_404(UserProfile, pk = userprofiles)
                setobject = Sets.objects.get(name = setname, userprofile = userprofiles).kanji.all().order_by(ordering)
                data = serializers.serialize("json",setobject)
            except KeyError:
                return HttpResponse("ajax error")
        return HttpResponse(simplejson.dumps(data), content_type="application/json")


                  
            
    
