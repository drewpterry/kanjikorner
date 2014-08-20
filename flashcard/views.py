from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji
from django.contrib.auth.models import User
from django.utils import simplejson
from django.core import serializers
from datetime import datetime
from django.core.context_processors import csrf


# Create your views here.
def practice_stack(request, full_name, set_name):
    if not request.user.is_authenticated() or request.user.username != full_name:
            return HttpResponse("you are not authenticated")
    else: 
        userprofiles = User.objects.get(username = full_name).userprofile.id
        userprofile = get_object_or_404(UserProfile, pk = userprofiles)
        kanjis = Sets.objects.get(name = set_name, userprofile = userprofiles).kanji.all()  
        return render(request, 'flashcard/practicecards.html', {'full_name':full_name, 'kanjis':kanjis} )