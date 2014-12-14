#profile
from django.conf.urls import patterns, url

from manageset import views

urlpatterns = patterns('',
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    # ex: /profile/
    url(r'^(?P<full_name>\w*)$', views.main_profile, name='index'),
    
    #four main views of new word, word bank, new kanji, and kanji bank
    url(r'^(?P<full_name>\w*)/new-kanji$', views.new_kanji_view, name='view_new_kanji'),
    url(r'^(?P<full_name>\w*)/new-set/known-kanji$', views.known_kanji_view, name='known-kanji'),
    url(r'^(?P<full_name>\w*)/new-set/new-words$', views.new_words_view, name='new-words'),
    url(r'^(?P<full_name>\w*)/new-set/word-bank$', views.word_bank_view, name='view_word_bank'),
    
    
    
    
    url(r'^new-set/view-known-words$', views.get_new_words, name='view_known_words'),
    url(r'^new-set/word-search$', views.word_search, name='wordsearch'),    
    url(r'^new-set/get-known-kanji$', views.get_known_kanji, name='get-known-kanji'),
    url(r'^new-set/get-word-bank$', views.get_word_bank, name='get_word_bank'),
    
    

    url(r'^(?P<full_name>\w*)/new-set/create-set$', views.add_words_to_set, name='create-set'),
 
    
    url(r'^(?P<full_name>\w*)/new-set/add-known-kanji$', views.add_known_kanji, name='add-known-kanji'),
    url(r'^(?P<full_name>\w*)/new-set/add-known-words$', views.add_known_words, name='add-known-words'),
    
    url(r'^(?P<full_name>\w*)/new-set/remove-known-kanji$', views.remove_known_kanji, name='remove-known-kanji'),



    url(r'^view-set/get-set-words$', views.view_stack_search, name='view_stack_search'),
    url(r'^(?P<full_name>\w*)/(?P<set_name>[-\w \']+)/view$', views.view_stack, name='view_stack'),
   
    
)   