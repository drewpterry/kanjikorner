from django.conf.urls import patterns, url
from flashcard.views import * 

urlpatterns =[ 
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    url(r'^srs$', view_srs_review, name='view-srs-review'),
    url(r'^srs/get$', get_srs_review, name='get-srs-review'),
    url(r'^update-word$', update_review_word, name='update_review_word'),
    url(r'^lvl-(\d{1,3})/(\d{1,2})$', view_review_deck, name='view-review-deck'),
    url(r'^lvl-(\d{1,3})/(\d{1,2})/get$', get_review_deck, name='get-review-deck'),
]   
