"""django_cache URL Configuration

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
from django_cache import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^people/add$', 'django_cache.view.add_people'),
    url(r'^people/get$', 'django_cache.view.get_people'),
    url(r'^people/update$', 'django_cache.view.update_people'),
    url(r'^people/delete$', 'django_cache.view.delete_people'),
    url(r'^people/select$', 'django_cache.view.select_people'),
]
