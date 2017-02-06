#overall site
from django.conf.urls import patterns, include, url
from manageset import views as manageset_views
from api import views as api_views
from admin_data_collection import views as admin_data_collection_views
from django.contrib import admin
from allauth.account.views import confirm_email as allauthemailconfirmation
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'sets', api_views.SetsViewSet)
router.register(r'word', api_views.WordsViewSet)
router.register(r'word-meanings', api_views.WordMeaningsViewSet)
router.register(r'known-words', api_views.KnownWordsViewSet)

admin.autodiscover()

urlpatterns = [ 
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
#namespace specifies exactly where url is coming from - inluded on index page
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/accounts/', include('allauth.urls')),
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', allauthemailconfirmation, name="account_confirm_email"),
    url(r'^$', manageset_views.index, name = "home"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^api/', include('manageset.urls', namespace='api')),
    url(r'^dashboard/', include('manageset.urls', namespace = "dashboard")),
    url(r'^profile/', include('manageset.urls', namespace = "profile")),
    url(r'^profile/', include('flashcard.urls', namespace = "flashcard")),
    url(r'^api/review/', include('flashcard.urls', namespace = "review")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^internal/', include('admin_data_collection.urls', namespace="admin_data_collection")),
]
