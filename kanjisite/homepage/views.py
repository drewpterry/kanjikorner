from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'homepage/index.html')
     

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user is not None:
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
    
def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/create-account/success')
    else:
        form = UserCreationForm()
    
    return render(request, 'homepage/create-account.html', {'form':form})  
    
    
def create_account_success(request):
    return render(request, 'homepage/create-account-success.html')      