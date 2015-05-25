from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import Kanji
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from forms import UserCreateForm
from manageset.models import UserProfile
from manageset.views import main_profile


# Create your views here.

def index(request):
    full_name = request.user.username
    c = {}
    c.update(csrf(request))
    template = 'homepage/index2.html'
    if request.user.is_authenticated():
        template = 'manageset/profile.html'
        return main_profile(request,full_name)
        
    thekanji = Kanji.objects.all()[0:2136]
        
    return render(request, template, {'full_name':full_name, 'kanji_objects': thekanji})
     

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    try:
        username = User.objects.get(email = username)
    except:
        return HttpResponseRedirect('/login/invalid')
    username = username.username
    user = auth.authenticate(username = username, password = password)
    if user is not None:
        # theusername = User.objects.get(username = username)
#         p = UserProfile(user = "testuser")
#         p.save()
        auth.login(request,user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/invalid')    
    
    # if user is not None:
#         auth.login(request,user)
#         request.session['validuser'] = 'hello'
#         return HttpResponseRedirect('/homepage/loggedin')
#     else:
#         return HttpResponseRedirect('/homepage/invalid')

def invalid_login(request):
    return render(request, 'homepage/invalid-login.html')
    
def logout(request):
    auth.logout(request)
    return index(request)    
    
def create_account(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            p = UserProfile(user = new_user)
            p.save()
            return HttpResponseRedirect('/create-account/success')
    else:
        form = UserCreateForm()
    
    return render(request, 'homepage/create-account.html', {'form':form})  
    
    
def create_account_success(request):
    return render(request, 'homepage/create-account-success.html')      