from django.conf.urls import patterns, url
from flashcard.views import * 

urlpatterns =[ 
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    url(r'^(?P<full_name>\w*)/(?P<set_name>[-\w ]+)/practice$', practice_stack, name='practice-stack'),
    url(r'^(?P<full_name>\w*)/(?P<set_name>[-\w ]+)/complete-stack$', complete_stack, name='complete-stack'),
    url(r'^(?P<full_name>\w*)/SRS-review$', srs_review_words, name='srs_review_words'),
    url(r'^(?P<full_name>\w*)/tier-level-update$', tier_level_update, name='tier_level_update'),



    url(r'^srs$', view_srs_review, name='view-srs-review'),
    url(r'^srs/get$', get_srs_review, name='get-srs-review'),
    url(r'^lvl-(\d{1,3})/(\d{1,2})$', view_review_deck, name='view-review-deck'),
    url(r'^lvl-(\d{1,3})/(\d{1,2})/get$', get_review_deck, name='get-review-deck'),
]   
