#profile
from django.conf.urls import patterns, url

from flashcard import views

urlpatterns = patterns('',
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    # ex: /profile/
    # url(r'^(?P<full_name>\w*)$', views.main_profile, name='index'),
    # url(r'^(?P<full_name>\w*)/new-set$', views.create_new_set, name='newset'),
#     url(r'^new-set/word-search$', views.word_search, name='wordsearch'),
#     url(r'^view-set/get-set-words$', views.view_stack_search, name='view_stack_search'),
#     url(r'^(?P<full_name>\w*)/new-set/create-set$', views.add_words_to_set, name='create-set'),
    url(r'^(?P<full_name>\w*)/(?P<set_name>[-\w ]+)/practice$', views.practice_stack, name='practice-stack'),
    url(r'^(?P<full_name>\w*)/(?P<set_name>[-\w ]+)/complete-stack$', views.complete_stack, name='complete-stack'),
    url(r'^(?P<full_name>\w*)/SRS-review$', views.srs_review_words, name='srs_review_words'),
    url(r'^(?P<full_name>\w*)/tier-level-update$', views.tier_level_update, name='tier_level_update'),
   
    
)   