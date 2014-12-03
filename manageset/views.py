# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji, KnownKanji
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Q
import json
from django.core import serializers
from datetime import datetime
from django.core.context_processors import csrf
from collections import deque
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
 
 
 
 
####################### NAVIGATION TO WORD AND KANJI VIEWS ################################        
# these four functions navigate to the four main pages when managing your sets: new words, word bank, new kanji, kanji bank            
def new_kanji_view(request,full_name):
    if verify_profiles(request,full_name) == False:
            return not_auth
    else:
        template='manageset/new_kanji_view.html'
        page_template='manageset/entry_index_page.html'
        # kanjis = Kanji.objects.all()
        profile = request.user.userprofile
        known_kanji_list = get_known_kanji_list(request)
        # print known_kanji_list, "hello"
        profile_known_kanji = Kanji.objects.all().exclude(pk__in = known_kanji_list).order_by('grade','id')
        # print profile_known_kanji, "test"
        if request.is_ajax():
            template = page_template
        
        return render(request, template, {'full_name':full_name, 'known_kanji': profile_known_kanji, 'page_template': page_template})


def word_bank_view(request,full_name):
    if verify_profiles(request,full_name) == False:
            return not_auth
    else:
        # kanjis = Kanji.objects.all()
        profile = request.user.userprofile
        profile_known_words = profile.known_words.all()
        return render(request, "manageset/known_word_bank.html", {'full_name':full_name, 'known_kanji': profile_known_words})           

def known_kanji_view(request,full_name):
    return render(request, "manageset/known_kanji_bank.html", {'full_name':full_name})
    
def new_words_view(request, full_name):
    return render(request, "manageset/new_words_view.html", {'full_name':full_name})        






##################################### AJAX REQUESTS ###################################################


def word_search(request):
    
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                ordering = request.GET['theorder']
                searchword = request.GET['searchword']
                kanji = Kanji.objects.filter(kanji_meaning__contains = searchword).order_by(ordering,'grade','id')
                data = serializers.serialize("json",kanji)
                data = json.loads(data)
                
                
                known_kanji_list = get_known_kanji_list(request)
                print known_kanji_list, "hello"
                for each in list(data):
                    
                    if each[u'pk'] in known_kanji_list:
                        known_kanji_list.remove(each[u'pk'])
                        data.remove(each)
                              
               
                data = data[:100]
                data = json.dumps(data)
                  
            except KeyError:
                return HttpResponse("error")    
                
        return HttpResponse(data, content_type="application/json")
   
   
def get_known_kanji_list(request):
    
    known_kanji_list = []
    profile = request.user.userprofile
    print profile.id
    # profile_known_kanji = profile.known_kanji.all()
    # profile_known_kanji =  KnownKanji.objects.filter(user_profile = profile.id).kanji.all()
    profile_known_kanji =  KnownKanji.objects.filter(user_profile = profile.id)
    # known_kanji_list.append(profile_known_kanji)
    for each in profile_known_kanji:
        theid = each.kanji.get().id
        known_kanji_list.append(theid)
 #        print known_kanji_list
    return known_kanji_list
        

#probably should rename
def get_known_kanji(request):
    
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                data = get_the_known_kanji(request)
                # kanjis = Kanji.objects.all()
                # data = []
#                 profile = request.user.userprofile.id
#                 profile_known_kanji = KnownKanji.objects.filter(user_profile = profile)
#                 for each in profile_known_kanji:
#                     kanji_obj = each.kanji.get()
#                     data.append(kanji_obj)
                data = serializers.serialize("json",data)
                data = json.dumps(data)


            except KeyError:
                return HttpResponse("error")
                
        return HttpResponse(data, content_type="application/json")



def get_the_known_kanji(request):
    data = []
    profile = request.user.userprofile.id
    profile_known_kanji = KnownKanji.objects.filter(user_profile = profile)
    for each in profile_known_kanji:
        kanji_obj = each.kanji.get()
        data.append(kanji_obj)
    # data = serializers.serialize("json",data)
#     data = json.dumps(data)
    return data
    


def get_word_bank(request):
    
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                # kanjis = Kanji.objects.all()
                profile = request.user.userprofile
                profile_known_words = profile.known_words.all().order_by('frequency', 'id')[0:200]
                data = serializers.serialize("json",profile_known_words)
                data = json.dumps(data)
                print data
            except KeyError:
                return HttpResponse("error")    
                
        return HttpResponse(data, content_type="application/json")                   
            

def get_known_word_list(request):
    
    known_word_list = []
    profile = request.user.userprofile
    profile_known_words = profile.known_words.all()
    
    for each in profile_known_words:
        known_word_list.append(each.id)
                  
    return known_word_list
    

def get_new_words(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                # ordering = request.GET['theorder']
                # searchword = request.GET['searchword']
               
                profile = request.user.userprofile
                # profile_known_kanji = profile.known_kanji.all()
                profile_known_kanji = get_the_known_kanji(request)
               
                kanji_in = []
                
                known_word_list = get_known_word_list(request)
                    
                for each in profile_known_kanji:
                    kanji_in.append(each.id)
                
                
                words = Words.objects.filter(kanji__in = kanji_in).exclude(frequency = 0).exclude(id__in = known_word_list).order_by('frequency','pk').distinct()[0:2000]
                
                data = serializers.serialize("json",words)
                data = json.loads(data)
                
                #add words with these kanji to front
                # new_kanji = [72,69,207,237,316]
                new_kanji = []
                words_with_new_kanji = []
                
                i = 0
                for each in list(data):
                    thelist = list(set(each[u'fields'][u'kanji'])-set(kanji_in))
                    if thelist:
                        data.remove(each)
                    else:
                        for kanji in new_kanji:
                            if kanji in each[u'fields'][u'kanji']:
                                # words_with_new_kanji.append(each)
                                data.remove(each)
                                data.insert(i,each)
                                i = i + 1
                                                                          
                data = data[:50]
                data = json.dumps(data)
                               
            except KeyError:
                return HttpResponse("there was an error")       
        return HttpResponse(data, content_type="application/json")
        


########################## ADD WORDS ####################################################        
                    
        
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
    
    for words in knownkanji:
        if UserProfile.objects.get(id = userprofiles).known_words.filter(id = words).exists() == False:
            obj1 = Words.objects.get(id = words)
            theknownkanji.append(obj1)
             
    userprofile.known_words.add(*theknownkanji)   
    #submit known kanji
    return new_words_view(request, full_name)



def add_known_kanji(request, full_name):    
    c = {}
    c.update(csrf(request))
    userprofiles = User.objects.get(username = full_name).userprofile.id
    userprofile = get_object_or_404(UserProfile, pk = userprofiles)
    knownkanji = request.POST.getlist('known-kanji')
    theknownkanji = []
            
    for kanjis in knownkanji:
        
        # if KnownKanji.objects.filter(user_profile = 10).kanji.filter(id = kanjis).exists() == False:
        obj1 = Kanji.objects.get(id = kanjis)
        new_known_kanji = KnownKanji(date_added = datetime.now())
        new_known_kanji.save()
        new_known_kanji.kanji.add(obj1)
        new_known_kanji.user_profile.add(userprofile)
            # KnownKanji.objects.get(user_profile = 10).kanji.add(obj1)
    
    print theknownkanji
    # userprofile.known_kanji.add(*theknownkanji)
    
    #submit known kanji
    return new_kanji_view(request, full_name)
    
   
#################################REMOVE WORDS####################################################

def remove_known_kanji(request,full_name):
    c = {}
    c.update(csrf(request))
    userprofiles = User.objects.get(username = full_name).userprofile.id
    # userprofile = get_object_or_404(UserProfile, pk = userprofiles)
    deletekanji = request.POST.getlist('chosenwords')
    print deletekanji
    thedeletekanji = []
    print KnownKanji.objects.filter(kanji__in = deletekanji, user_profile = userprofiles).delete()
    print thedeletekanji
    # profile = request.user.userprofile
  #   profile_known_kanji = profile.known_kanji.all().order_by('grade', 'id')
    # print KnownKanji.objects.get(user_profile = 8)
    # userprofile.known_kanji.filter(id = 116).delete()
    # print UserProfile.objects.get(id = userprofiles).known_kanji.filter(id = 1126).delete()
    print "hello"
    return known_kanji_view(request, full_name)
    
    
###################################STACK EDITING#################################
         
    
    
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


                  
            
    
