"""
Definition of urls for globepost.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from newsapp import urls
# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^app$', 'app.views.home', name='home'),
    #url(r'^index1$', 'newsapp.views.test', name='test'),
    #url(r'^test1$', 'newsapp.views.test1', name='test1'),
    #url(r'^test2$', 'newsapp.views.test2', name='test2'),
    url(r'^test4$', 'newsapp.views.test4', name='test4'),
     url(r'^(?P<section>\w+)$', 'newsapp.views.ajax1', name='ajax1'),
    #url(r'^contact$', 'app.views.contact', name='contact'),
    #url(r'^about', 'app.views.about', name='about'),
    #url(r'^login/$',
    #    'django.contrib.auth.views.login',
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title':'Log in',
    #            'year':datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    'django.contrib.auth.views.logout',
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$',include('newsapp.urls')),
    #url(r'^(?P<section>\w+)$', 'newsapp.views.home2', name='home2'),
)
