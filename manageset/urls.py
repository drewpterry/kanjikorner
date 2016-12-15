from django.conf.urls import patterns, url
from manageset import views

urlpatterns = [
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    url(r'^$', views.view_dashboard, name='dashboard'),    
    url(r'^all-decks/get$', views.get_master_review_decks, name='all-decks'),    
    url(r'^dashboard-data/get$', views.get_dashboard_data, name='dashboard-data'),    
]   
