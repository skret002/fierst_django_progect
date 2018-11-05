# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from . import views

 
urlpatterns =  [
    url(r'^print_photo/$', views.print_photo_home, name='print_photo_home'),
    url(r'^print_photo_order/$', views.print_photo_order, name='print_photo_order'),


    ]