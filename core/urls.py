from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^question/create/$', ContactCreateView.as_view(), name='contact_form'),
  url(r'^success/$', Success.as_view(), name='success'),
  url(r'^about_me/$', About_Me.as_view(), name='about_me'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
)