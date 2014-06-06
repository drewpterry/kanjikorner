from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import UserProfile, Sets, Words, Kanji
from django.contrib.auth.models import User
# import pdb; pdb.set_trace()

# Create your views here.

def main_profile(request,full_name):
    userprofile = User.objects.get(username = full_name).userprofile.id
    return render(request,'manageset/profile.html', {'full_name':full_name, 'userprofileid':userprofile})
