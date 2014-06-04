#overall site
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
#namespace specifies exactly where url is coming from - inluded on index page
    url(r'^$', 'homepage.views.index'),
    url(r'^create-account/', include('homepage.urls', namespace = "login")),
    url(r'^login/', include('homepage.urls', namespace = "login")),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)