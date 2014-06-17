#profile
from django.conf.urls import patterns, url

from manageset import views

urlpatterns = patterns('',
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    # ex: /profile/
    url(r'^(?P<full_name>\w*)$', views.main_profile, name='index'),
    url(r'^(?P<full_name>\w*)/new-set$', views.create_new_set, name='newset'),
    url(r'^new-set/word-search$', views.word_search, name='wordsearch'),
    url(r'^(?P<full_name>\w*)/new-set/create-set$', views.add_words_to_set, name='create-set'),
    url(r'^(?P<full_name>\w*)/(?P<set_name>[-\w ]+)/view$', views.view_stack, name='view_stack'),
   
    
)   