from django.conf.urls import patterns, url
from manageset import views

urlpatterns = [
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    url(r'^/$', views.view_dashboard, name='dashboard'),    
]   
