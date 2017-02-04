from django.conf.urls import patterns, url
from flashcard.views import * 

urlpatterns =[ 
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    url(r'^srs/get$', get_srs_review),
    url(r'^review-deck-complete$', review_deck_complete),
    url(r'^update-word$', update_review_word),
    url(r'^lvl-(\d{1,3})/(\d{1,2})/get$', get_review_deck),
]   
