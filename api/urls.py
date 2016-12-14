from django.conf.urls import patterns, url
from api import views

urlpatterns = [
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    url(r'^all-decks$', views.get_master_review_decks, name='dashboard'),    
    # url(r'^all-decks/get$', views.get_master_review_decks, name='all-decks'),    
]   
