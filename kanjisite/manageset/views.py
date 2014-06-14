from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
from datetime import datetime
# import pdb; pdb.set_trace()

# Create your views here.

def main_profile(request,full_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
            # return render(request, 'myapp/login_error.html')
            return HttpResponse("you are not authenticated")
    else:        
        userprofiles = User.objects.get(username = full_name).userprofile.id
        userprofile = get_object_or_404(UserProfile, pk = userprofiles)
        return render(request,'manageset/profile.html', {'full_name':full_name, 'usersets':userprofile})
        
        
def create_new_set(request,full_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
            # return render(request, 'myapp/login_error.html')
            return HttpResponse("you are not authenticated")
    else:
        kanjis = Kanji.objects.all()
        return render(request, "manageset/create-set.html", {'full_name':full_name, 'kanjis':kanjis})   
        

def word_search(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                ordering = request.GET['theorder']
                kanji = Kanji.objects.all().order_by(ordering)
                data = serializers.serialize("json",kanji)
            except KeyError:
                return HttpResponse("error")    
        # dump = simplejson.dumps(kanji)   
        return HttpResponse(simplejson.dumps(data), content_type="application/json")   
        # return HttpResponse("hello")
        
        
def add_words_to_set(request,full_name):
    userprofiles = User.objects.get(username = full_name).userprofile.id
    userprofile = get_object_or_404(UserProfile, pk = userprofiles)
    setname = request.GET['title']
    description = request.GET['description']
    chosenwords = request.GET.getlist('chosenwords')
    thechosenwords = []
    for kanji in chosenwords:
        obj1 = Kanji.objects.get(id = kanji)
        thechosenwords.append(obj1)
        
    newset = Sets(name = setname, description = description, pub_date = datetime.now())
    newset.save()
    newset.kanji.add(*thechosenwords)
    userprofile.user_sets.add(newset)
    return render(request, "manageset/create-set-confirm.html", {'setname':setname, 'chosenwords':thechosenwords})        
    
