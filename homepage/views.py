from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from manageset.models import Kanji
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from forms import UserCreateForm
from manageset.models import UserProfile
from manageset.views import view_dashboard 

def index(request):
    full_name = request.user.username
    c = {}
    c.update(csrf(request))
    template = 'homepage/index.html'
    if request.user.is_authenticated():
        return view_dashboard(request)
    return view_dashboard(request)
    # return render(request, template, {'full_name':full_name})
     

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

        auth.login(request,user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/invalid')    
    

def invalid_login(request):
    not_valid = True
    return render(request, 'registration/login.html', {'not_valid':not_valid})
    
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
    
def faq_page(request):
	return render(request, 'homepage/faq.html') 
    
def contact_us_page(request):
	return render(request, 'homepage/contact.html')

def highscores_page(request):
    return render(request, 'homepage/highscores.html')       
