from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
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
        

def word_search(request, full_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
        return HttpResponse("You are not authenticated")
    else:
        if request.is_ajax():
            try:
                ordering = request.POST['theorder']
                kanji = Kanji.objects.all().order_by(ordering)
                data = serializers.serialize("json",kanji)
            except KeyError:
                return HttpResponse("error")    
        # dump = simplejson.dumps(kanji)   
        return HttpResponse(simplejson.dumps(data), content_type="application/json")   
        # return HttpResponse("hello")
        
        
def add_words_to_set(request,full_name):
    setname = request.GET['title']
    return HttpResponse("You created a new set!" + setname + "called.")        
    
