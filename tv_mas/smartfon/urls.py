# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from . import views

 
urlpatterns =  [
    url(r'remont_smartfonov.html/$', views.smartfon_home_and_search, name='smartfon_home_and_search'),
    url(r'remont_smartfonov_result.html/$', views.smarfon_search_result, name='smarfon_search_result'),
    url(r'remont_smartfona/(?P<brend>[^/]+)/(?P<model_name>[^/]+)/(?P<model_id>[^/]+)/(?P<page_number>[^/]+)/$', views.SmartfonService, name='SmartfonService'),
    #url(r'remont_smartfona/$', views.SmartfonService, name='SmartfonService'),
    url(r'remont_smartfonov_cart.html/(?P<name_part>[^/]+)/$', views.SalePartsCart, name='SalePartsCart'),
    url(r'remont_smartfonov_cart.html/(?P<model_name>[^/]+)/(?P<model_id>[^/]+)/(?P<problem>[^/]+)/$', views.PartsCart, name='PartsCart'),

]