# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji, KnownKanji, KnownWords
from django.db.models import Count, Min, Sum, Avg
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Q
import json
from flashcard.views import srs_get_and_update
from django.core import serializers
from datetime import datetime, timedelta
import time
from django.core.context_processors import csrf
from collections import deque
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_control
# import pdb; pdb.set_trace()

# Create your views here.

def verify_profiles(request,full_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
            # return render(request, 'myapp/login_error.html')
            return False
            
not_auth = HttpResponse("you are not authenticated")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def main_profile(request,full_name):
    if verify_profiles(request,full_name) == False:
            return not_auth
    else:
        
        userprofiles = User.objects.get(username = full_name).id
       
        userprofile = UserProfile.objects.get(user = userprofiles)
        usersets = userprofile.user_sets.all().order_by('pub_date')
        
        
        
        # userprofile = get_object_or_404(UserProfile, pk = userprofiles)
        user_known_words = KnownWords.objects.filter(user_profile = userprofile)
        known_words = user_known_words.values('tier_level').annotate(count = Count('tier_level')).order_by('tier_level')
        total_word_count = user_known_words.exclude(tier_level__in = [0,10]).count()
        one_day_ago = datetime.now() - timedelta(days = 1)
        number_words_added_today = KnownWords.objects.filter(user_profile = userprofile, date_added__gte = one_day_ago).count()
        total_review_right = user_known_words.aggregate(Sum('times_answered_correct'))
        total_review_wrong = user_known_words.aggregate(Sum('times_answered_wrong'))
        total_reviews_ever = total_review_wrong['times_answered_wrong__sum'] + total_review_right['times_answered_correct__sum']
        # print number_words_added_today
        # print total_word_count, "ehll"
        
        
        # print known_words[0]['tier_level']
        
        count_dict = {}
        
        for each in known_words:
            count_dict[each['tier_level']] = each['count']
            
        for each in range(10):
            # each['tier_level']] = each['count']
            try:
                count_dict[each]
            except KeyError:
                count_dict[each] = 0
                
        number_of_added_kanji =  KnownKanji.objects.filter(user_profile = userprofile).count()
        # print number_of_added_kanji
       
        
        number_of_reviews = len(srs_get_and_update(request, full_name))
        next_review = KnownWords.objects.filter(user_profile = userprofile, time_until_review__range = (0,86400)).values('time_until_review').order_by('time_until_review')
        due_tomorrow = len(next_review) + number_of_reviews
        if number_of_reviews == 0:
            # next_review = KnownWords.objects.filter(user_profile = userprofile, time_until_review__range = (0,86400)).values('time_until_review').order_by('time_until_review')
            if next_review.exists():
                next_review = next_review[0]
                # print next_review
                next_review = next_review['time_until_review']

                next_review = str(timedelta(seconds = next_review)).split('.')[0]
        else:
            next_review = "Now"
            
            
        
        
        
        return render(request,'manageset/profile.html', {'full_name':full_name, 'usersets':usersets, 'review_number': number_of_reviews, \
         'the_count':count_dict, 'next_review':next_review, 'due_tomorrow':due_tomorrow, 'added_kanji_count': number_of_added_kanji,\
          'word_count':total_word_count, 'words_added_today':number_words_added_today, 'total_reviews_ever':total_reviews_ever})
 
 
 
 
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
        # profile_known_words = profile.known_words.all()
        profile_known_words = 2
        return render(request, "manageset/known_word_bank.html", {'full_name':full_name, 'known_kanji': profile_known_words})           



def known_kanji_view(request,full_name):
    profile = request.user.userprofile
    known_kanji = KnownKanji.objects.filter(user_profile = profile, selected_kanji = True)
    
    known_kanji_list = []
    for each in known_kanji:
        known_kanji_list.append(each.kanji.get().id)
        
    print known_kanji_list    
    # print known_kanji
    return render(request, "manageset/known_kanji_bank.html", {'full_name':full_name, 'known_kanji_list':known_kanji_list})
 
 
 
    
def new_words_view(request, full_name):
    
    template='manageset/new_words_view.html'
    page_template='manageset/entry_index_words.html'
    profile = request.user.userprofile
    
    # profile_known_kanji = profile.known_kanji.all()
    # these two callbacks also add like half a second
    
    usersets = profile.user_sets.all().count()
    kanji_in = get_known_kanji_list(request)

    known_word_list = get_known_word_list(request, True)
    # print known_word_list
    # kanji_in = []
    # exclude_kanji = []
    # m = 200
    # while (m < 2000):
       # print 'The count is:', m
       # kanji_in.append(m)
       # m = m + 1
    # print exclude_kanji
    

    # start = time.clock()
    
#--------------------------------1st way-------------------------------------------------------------------------------------------------------    
    #executing this query will take a long long time...only works if it gets sent straight to browser...very slow until you add enough kanji...4s if you add 410 but slows down after that, which means works best when you have a lot of kanji in your bank
   
    # exclude_kanji = Kanji.objects.values('id').exclude(id__in = kanji_in)
 #    print "the length of exclude kanji", len(exclude_kanji)
 #    exclude_kanji = []
 #
 #    i = 20
 #    for each in range(1,200):
 #        exclude_kanji.append(each)
 #        i + 1
 #
 #    print "----------------------------------------------------------------------------- ", exclude_kanji
 #    words = Words.objects.exclude(kanji__in = exclude_kanji).exclude(frequency = 0).exclude(id__in = known_word_list).order_by('frequency')[0:100]
 #
 #    data = words
 #--------------------------------end 1st way-------------------------------------------------------------------------------------------------------
 #    data = words
    
    # print words
    # print len(words)
    # i = 0
#     for each in words:
#         i = i + 1
#
#     print i 
    # print exclude_words
    # print exclude_kanji
    # print len(exclude_words)
    # print len(exclude_words)
    # print len(exclude_words)
 #    for each in exclude_kanji:
 #        print each
 #    elapsed = (time.clock() - start)
 #    print "exclude query ", elapsed
    # print exclude_words
      
    # start = time.clock()
    #this query add in another exclude to remove words that have extra kanji makes it a lot slower
    # words = Words.objects.filter(kanji__in = kanji_in).exclude(frequency = 0).exclude(id__in = known_word_list).order_by('frequency').prefetch_related('kanji').distinct()[0:1000]
    # print Words.objects.filter(kanji__in = kanji_in).exclude(frequency = 0).exclude(id__in = known_word_list).order_by('frequency').prefetch_related('kanji').distinct()[0:100].query
    # words = Words.objects.exclude(frequency = 0).exclude(kanji__in = exclude_kanji).exclude(id__in = known_word_list).order_by('frequency').distinct()[0:1000]
    # print "all words : ", words
    # print Words.objects.exclude(frequency = 0).exclude(kanji__in = exclude_kanji).exclude(id__in = known_word_list).order_by('frequency').distinct()[0:1000]
    # print words
    # print words
    # elapsed = (time.clock() - start)
    # print "database query time: ", elapsed
    
    
    

    
    
    
    #start different way -------------------------------------------------------------
    
    # all lot faster in general but only gives small subset of results, not effective for finding words with specific kanji because only pulls from returned number...as long as their are not too many kanji it happens quickly, no problem with 90 kanji after that time starts rising considerably
    # kanji_in = []
#     for each in range(20,600):
#         kanji_in.append(each)
    
    

    selected_kanji = KnownKanji.objects.filter(user_profile = profile, selected_kanji = True).prefetch_related('kanji')
    
    new_kanji = []
    for each in selected_kanji:
        new_kanji.append(each.kanji.get().id)

    special_words = Words.objects.filter(kanji__in = new_kanji).exclude(frequency_two = None).exclude(published = False).exclude(id__in = known_word_list).exclude(frequency_two__lte = 300, frequency = 0).prefetch_related('kanji').order_by('-frequency_two')
    # special_words = Words.objects.filter(kanji__in = new_kanji).exclude(frequency = 0).exclude(id__in = known_word_list).prefetch_related('kanji').order_by('frequency')
    special_words = list(special_words)
    for each in list(special_words):
        kanji = each.kanji.all()
        id_list = set()
        for kanji_id in kanji:
            id_list.add(kanji_id.id)

        the_list = list(id_list - set(kanji_in))

        if the_list:
            special_words.remove(each)


    if len(special_words) == 0:        

        words = Words.objects.filter(kanji__in = kanji_in).exclude(frequency_two = None).exclude(id__in = known_word_list).exclude(published = False).exclude(Q(frequency_two__lte = 300), Q(frequency = 0)|Q(frequency__gte = 35)).order_by('-frequency_two').prefetch_related('kanji').distinct()[0:1000]
        # words = Words.objects.filter(kanji__in = kanji_in).exclude(frequency = 0).exclude(id__in = known_word_list).order_by('frequency').prefetch_related('kanji').distinct()[0:1000]
        words_list = list(words)
     
        i = 0
        for each in list(words):
        
            kanji = each.kanji.all()
            id_list = set()
            for kanji_id in kanji:
                id_list.add(kanji_id.id)
        
        
            the_one_list = list(id_list - set(kanji_in))
        
            if the_one_list:
                words_list.remove(each)
        
    else:
        words_list = []





    data = special_words + words_list

    for each in selected_kanji.all():
        for kanji in each.kanji.all():
            print kanji
    
    
    if request.is_ajax():
        template = page_template               
    return render(request, template, {'full_name':full_name, 'data':data, 'page_template':page_template, 'usersets':usersets, 'selected_kanji':selected_kanji})        




##################################### AJAX REQUESTS ###################################################

# THIS IS CURRENTLY NOT BEING USED, REPLACED IT WITH KANJI VIEW FUNCTION, IF ADDING SEARCH OR FILTER SHOULD REUSE THIS
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
                # data = json.dumps(data)

            except KeyError:
                return HttpResponse("error")

        return HttpResponse(data, content_type="application/json")
   
   
def get_known_kanji_list(request):

    known_kanji_list = []
    profile = request.user.userprofile
    
    profile_known_kanji =  KnownKanji.objects.filter(user_profile = profile.id).prefetch_related('kanji')
    
    for each in profile_known_kanji:
        theid = each.kanji.get().id
        known_kanji_list.append(theid)

    return known_kanji_list
        

#probably should rename
def get_known_kanji(request):
    
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                
                data = get_the_known_kanji(request)
               
                data = serializers.serialize("json",data)
                data = json.dumps(data)


            except KeyError:
                return HttpResponse("error")
                
        return HttpResponse(data, content_type="application/json")


# i dont think this is being used anymore
def get_the_known_kanji(request):
    data = []
    profile = request.user.userprofile.id
    profile_known_kanji = KnownKanji.objects.filter(user_profile = profile).prefetch_related('kanji').order_by('date_added').reverse()
    # print profile_known_kanji
    # print profile_known_kanji
    for each in profile_known_kanji:
        kanji_obj = each.kanji.get()
        data.append(kanji_obj)
    # data = serializers.serialize("json",data)
#     data = json.dumps(data)

    # print "known kanji data", data
    return data
    


def get_word_bank(request):
    
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                
                data = get_known_word_list(request, False)
                
                data = serializers.serialize("json",data)
                data = json.dumps(data)
            except KeyError:
                return HttpResponse("error")    
                
        return HttpResponse(data, content_type="application/json")                   
            



def get_known_word_list(request, withid):
    
    known_word_list = []
    profile = request.user.userprofile.id
    profile_known_kanji = KnownWords.objects.filter(user_profile = profile).order_by('date_added')
 
    if withid == False:
        for each in profile_known_kanji:
            # print each.date_added, each.words
            kanji_obj = each.words
            known_word_list.append(kanji_obj)
    else:
        for each in profile_known_kanji:
            # print each.date_added
            kanji_obj = each.words.id
            known_word_list.append(kanji_obj)
                            
    return known_word_list
    
    
    
    
# i dont think this currently does anything
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

                known_word_list = get_known_word_list(request, True)
                # print known_word_list

                # exclude_kanji = []
 #                m = 1000
 #                while (m < 2000):
 #                   # print 'The count is:', m
 #                   exclude_kanji.append(m)
 #                   m = m + 1
                # print exclude_kanji
                print "this is the get new words function"

                for each in profile_known_kanji:
                    kanji_in.append(each.id)

                #this is the query that takes forever, adding another exclude to remove words that have extra kanji makes it a lot slower
                words = Words.objects.filter(kanji__in = kanji_in).exclude(frequency = 0).exclude(id__in = known_word_list).order_by('frequency','pk').distinct()[0:1000]
                # print words

                #i think this is what causes it to slow down
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
                        # i = i + 1
                    else:
                        for kanji in new_kanji:
                            if kanji in each[u'fields'][u'kanji']:
                                # words_with_new_kanji.append(each)
                                data.remove(each)
                                data.insert(i,each)
                                i = i + 1
                # print i, "hello"
                data = data[:10]
                data = json.dumps(data)

                # print KnownWords.objects.all()[0].words
            except KeyError:
                return HttpResponse("there was an error")
        return HttpResponse(data, content_type="application/json")
        


def update_knownkanji_special(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                profile = request.user.userprofile.id
                theid = request.GET['theid']
                
                data = KnownKanji.objects.filter(user_profile = profile, kanji = theid)
                # data = list(data)
                for each in data:
                    if each.selected_kanji == False:
                        each.selected_kanji = True
                    else:
                        each.selected_kanji = False    
                    each.save()        
                
                
                # data = get_known_word_list(request, False)
                
                data = serializers.serialize("json",data)
                data = json.dumps(data)
            except KeyError:
                return HttpResponse("error")    
                
        return HttpResponse(data, content_type="application/json")     
    return




########################## ADD WORDS ####################################################        
                    
        
def add_words_to_set(request,full_name):
    c = {}
    c.update(csrf(request))
    userprofiles = User.objects.get(username = full_name).userprofile.id
    userprofile = get_object_or_404(UserProfile, pk = userprofiles)
    setname = request.POST['title']
    # description = request.POST['description']
    description = ''
    
    chosenwords = request.POST.getlist('chosenwords')
    thechosenwords = []
    print thechosenwords, "hello"
    for words in chosenwords:
        obj1 = Words.objects.get(id = words)
        new_known_kanji = KnownWords(words = obj1, user_profile = userprofile, date_added = datetime.now(), tier_level = 0, last_practiced = datetime.now())
        new_known_kanji.save()
        thechosenwords.append(obj1)
        
    newset = Sets(name = setname, description = description, pub_date = datetime.now(), times_practiced = 0)
    newset.save()
    newset.words.add(*thechosenwords)
    userprofile.user_sets.add(newset)
    return HttpResponseRedirect(reverse('profile:index', kwargs = {'full_name':full_name}))
    # return render(request, "manageset/create-set-confirm.html", {'setname':setname, 'chosenwords':thechosenwords})


# def add_known_words(request, full_name):
#     c = {}
#     c.update(csrf(request))
#     userprofiles = User.objects.get(username = full_name).userprofile.id
#     userprofile = get_object_or_404(UserProfile, pk = userprofiles)
#     knownkanji = request.POST.getlist('known-kanji')
#     theknownkanji = []
#
#     # for words in knownkanji:
#  #        if UserProfile.objects.get(id = userprofiles).known_words.filter(id = words).exists() == False:
#  #            obj1 = Words.objects.get(id = words)
#  #            theknownkanji.append(obj1)
#  #
#  #    userprofile.known_words.add(*theknownkanji)
#     #submit known kanji
#
#     print knownkanji
#
#     for wordss in knownkanji:
#
#         # if KnownKanji.objects.filter(user_profile = 10).kanji.filter(id = kanjis).exists() == False:
#         obj1 = Words.objects.get(id = wordss)
#         new_known_kanji = KnownWords(words = obj1, user_profile = userprofile, date_added = datetime.now(), tier_level = 10, last_practiced = datetime.now())
#         new_known_kanji.save()
#         # new_known_kanji.words.add(obj1)
# #         new_known_kanji.user_profile.add(userprofile)
#
#
#
#     return new_words_view(request, full_name)
    

def add_known_word(request, full_name):    
    c = {}
    c.update(csrf(request))
    
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                profile = request.user.userprofile
                word_id = request.POST['word_id']
                obj1 = Words.objects.get(id = word_id)
                
                new_known_word = KnownWords(words = obj1, user_profile = profile, date_added = datetime.now(), tier_level = 10, last_practiced = datetime.now())
                # print "hello"
                new_known_word.save()
                data = 1
            except KeyError:
                return HttpResponse("error")    
                
        return HttpResponse(data, content_type="application/json")
    
    return    





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

    deletekanji = request.POST.getlist('chosenwords')
    # print deletekanji, "not work"
    for each in deletekanji:
        the_kanji_object = Kanji.objects.get(id = each)
        print the_kanji_object
        KnownKanji.objects.get(user_profile = userprofiles, kanji = the_kanji_object).delete()
    
    return known_kanji_view(request, full_name)
    

def remove_known_word(request, full_name):    
    c = {}
    c.update(csrf(request))
    
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                profile = request.user.userprofile
                word_id = request.POST['word_id']
                the_word = Words.objects.get(id = word_id)
                obj1 = KnownWords.objects.get(user_profile = profile, words = the_word)
                obj1.delete()
                # print "hello"
                
                data = 1
            except KeyError:
                return HttpResponse("error")    
                
        return HttpResponse(data, content_type="application/json")
    
    return    
    
    
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


                  
            
    
