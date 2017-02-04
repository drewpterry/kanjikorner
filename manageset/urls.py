from django.conf.urls import patterns, url
from manageset import views

urlpatterns = [
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    url(r'^$', views.index),    
    url(r'^all-decks/get$', views.get_master_review_decks),    
    url(r'^user-decks/get$', views.get_user_sets),    
    url(r'^profile-data/get$', views.get_profile_data),    
    url(r'^review-data/get$', views.get_review_data),    
    url(r'^chart-data/get$', views.get_chart_data),    
]   
