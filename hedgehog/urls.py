"""hedgehog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sites.models import Site
from django import views
from pages import views as viewsPages
from mailers import views as viewsMailers
from faq import views as viewsFaq
from . import settings

urlpatterns = [
    #url(r'^o-studii/$', views.flatpage, {'url': '/o-studii/'}, name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', viewsPages.home, name = "homepage"),
    url(r'^pages/', include('pages.urls', namespace="pages")),
    url(r'^sendmessage/$', viewsMailers.sendmessage, name="sendmessage"),
    url(r'^spasibo/$', viewsMailers.thankyou, name="thankyou"),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^gallery/', include('imagestore.urls', namespace='imagestore')),
    url(r'^faq/', include('faq.urls', namespace='faq')),
    url(r'^studio/$', viewsPages.studio, name='o-studii'),
    url(r'^training/$', viewsPages.training, name='training'),
    url(r'^contacts/$', viewsPages.contacts, name='contact'),

    #url(r'^(?P<url>.*/)$', views.flatpage),
]