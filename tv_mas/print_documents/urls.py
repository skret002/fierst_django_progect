# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from . import views

 
urlpatterns =  [
    url(r'^print_docs/$', views.print_doc_home, name='print_doc_home'),
    url(r'^print_docs_order/$', views.print_doc_order, name='print_doc_order'),


    ]