# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from . import views

 
urlpatterns =  [
    url(r'^PHOTOS_OF_THE_DOCUMENTS/$', views.photo_home, name='photo_home'),
    url(r'^ORDER_PHOTO/$', views.photo_order, name='photo_order'),


    ]