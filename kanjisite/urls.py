#overall site
from django.conf.urls import patterns, include, url
from manageset import views
from homepage import views as homepage_views
from admin_data_collection import views as admin_data_collection_views
from django.contrib import admin
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView
admin.autodiscover()

urlpatterns = [ 
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
#namespace specifies exactly where url is coming from - inluded on index page
    url(r'^$', homepage_views.index, name = "home"),
    url(r'^faq/', homepage_views.faq_page, name = "faq"),
    url(r'^highscores/', homepage_views.highscores_page, name = "high-scores"),
    url(r'^contact/', homepage_views.contact_us_page, name = "contact-us"),
    url(r'^create-account/', include('homepage.urls', namespace = "create-account")),
    url(r'^login/', include('homepage.urls', namespace = "login")),
    url(r'^logout/', include('homepage.urls', namespace = "logout")),
    url(r'^profile/', include('manageset.urls', namespace = "profile")),
    url(r'^profile/', include('flashcard.urls', namespace = "flashcard")),
    url(r'^review/', include('flashcard.urls', namespace = "review")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^register/$',RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),name='registration_register'),
    url(r'^internal/', include('admin_data_collection.urls', namespace="admin_data_collection")),
]
