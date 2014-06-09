#profile
from django.conf.urls import patterns, url

from manageset import views

urlpatterns = patterns('',
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    # ex: /profile/
    url(r'^(?P<full_name>\w*)$', views.main_profile, name='index'),
    url(r'^(?P<full_name>\w*)/new-set$', views.create_new_set, name='newset'),
   
    
)   