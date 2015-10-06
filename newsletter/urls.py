from django.conf.urls import url, patterns
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
)
