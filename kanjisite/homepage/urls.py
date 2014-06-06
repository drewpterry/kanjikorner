#homepage
from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('',
#url takes four arguments - regex (searches for matching term), view, kwargs, name (naming urls)
    # ex: /login/
    url(r'^$', views.create_account, name='index'),
    url(r'^success/$', views.create_account_success),
    url(r'^complete/$', views.logout),
    # url(r'^login/$', views.login, name = 'login'),
    url(r'^auth/$', views.auth_view),
    url(r'^invalid/$', views.invalid_login),
#     url(r'^logout/$', views.logout),
#     url(r'^loggedin/$', views.loggedin),
#     url(r'^invalid/$', views.invalid_login),
#     url(r'^register/$', views.register_user),
#     url(r'^register_success/$', views.register_success),
    
)    