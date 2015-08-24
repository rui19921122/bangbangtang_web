"""website URL Configuration

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
from mobile.views import index,search,login_in,register,order,course,comment_list,account,log_out




urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^search$',search,name='search'),
    url(r'^login',login_in),
    url(r'^logout',log_out),
    url(r'^register',register),
    url(r'^order',order),
    url(r'^course/(?P<course_id>\d{1,5})$',course,name='course'),
    url(r'^course_detail/(?P<course_id>\d{1,5})$',course,name='course_detail'),
    url(r'^comment_list/(?P<course_id>\d{1,5})$',comment_list,name='comment_list'),
    url(r'^account$',account, name='account'),
]
