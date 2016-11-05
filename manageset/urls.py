from django.conf.urls import patterns, url
from manageset import views

urlpatterns = [
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    # ex: /profile/
    url(r'^(?P<full_name>\w*)$', views.main_profile, name='index'),

    
    #four main views of new word, word bank, new kanji, and kanji bank
    url(r'^(?P<full_name>\w*)/new-kanji$', views.new_kanji_view, name='view_new_kanji'),
    url(r'^(?P<full_name>\w*)/new-set/known-kanji$', views.KnownKanjiView.as_view(), name='known-kanji'),
    url(r'^(?P<full_name>\w*)/new-set/known-kanji-filter$', views.KnownKanjiFilter.as_view(), name='known-kanji-filter'),
    url(r'^(?P<full_name>\w*)/new-set/new-words$', views.new_words_view, name='new-words'),
    url(r'^(?P<full_name>\w*)/new-set/word-bank$', views.word_bank_view, name='view_word_bank'),
    url(r'^(?P<full_name>\w*)/new-set/all-words$', views.all_words, name='all_words'),
    url(r'^(?P<full_name>\w*)/new-set/selected-words$', views.selected_words_view, name='selected_words'),
    url(r'^(?P<full_name>\w*)/update-words-practiced-today$', views.update_words_practiced_today, name='update_words_practiced_today'),
    
    
    url(r'^new-set/word-search$', views.word_search, name='wordsearch'),    
    url(r'^new-set/get-known-kanji$', views.get_known_kanji, name='get-known-kanji'),
    url(r'^new-set/get-word-bank$', views.get_word_bank, name='get_word_bank'),
    
    url(r'^(?P<full_name>\w*)/new-set/create-set$', views.add_words_to_set, name='create-set'),
 
    url(r'^(?P<full_name>\w*)/new-set/add-known-kanji$', views.add_known_kanji, name='add-known-kanji'),
    url(r'^(?P<full_name>\w*)/new-set/add-known-word$', views.add_known_word, name='add-known-word'),
    
     url(r'^(?P<full_name>\w*)/new-set/remove-known-word$', views.remove_known_word, name='remove-known-word'),
    url(r'^(?P<full_name>\w*)/new-set/remove-known-kanji$', views.remove_known_kanji, name='remove-known-kanji'),
    url(r'^upate-knownkanji-special$', views.update_knownkanji_special, name='update-knownkanji-special'),

    url(r'^view-set/get-set-words$', views.view_stack_search, name='view_stack_search'),
    url(r'^(?P<full_name>[-\w]+)/(?P<set_name>[-\w \']+)/view$', views.view_stack, name='view_stack'),
]   
