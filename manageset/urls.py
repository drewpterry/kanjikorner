from django.conf.urls import patterns, url
from manageset import views

urlpatterns = [
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    url(r'^$', views.view_dashboard, name='dashboard'),    
    url(r'^all-decks/get$', views.get_master_review_decks, name='all-decks'),    
    url(r'^profile-data/get$', views.get_profile_data, name='profile-data'),    
    url(r'^review-data/get$', views.get_review_data, name='review-data'),    
]   
