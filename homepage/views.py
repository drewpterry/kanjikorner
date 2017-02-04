from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import Kanji
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from forms import UserCreateForm
from manageset.models import UserProfile
# from manageset.views import view_dashboard 

# def index(request):
    # full_name = request.user.username
    # c = {}
    # c.update(csrf(request))
    # template = 'homepage/index.html'
    # if request.user.is_authenticated():
        # return view_dashboard(request)
    # return view_dashboard(request)
    # return render(request, template, {'full_name':full_name})
     

