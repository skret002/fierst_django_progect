# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from . import views

 
urlpatterns =  [
    url(r'remont_notebook.html/$', views.notebook_home_and_search, name='notebook_home_and_search'),
    url(r'remont_notebook_result.html/$', views.notebook_search_result, name='notebook_search_result'),
    url(r'remont_notebook/(?P<brend>[^/]+)/(?P<model_name>[^/]+)/(?P<model_id>[^/]+)/(?P<page_number>[^/]+)/$', views.NotebookService, name='NotebookService'),
    #url(r'remont_smartfona/$', views.SmartfonService, name='SmartfonService'),
    url(r'remont_notebook_cart.html/(?P<name_part>[^/]+)/$', views.SalePartsCart, name='SalePartsCart'),
    url(r'remont_notebook_cart.html/(?P<model_name>[^/]+)/(?P<model_id>[^/]+)/(?P<problem>[^/]+)/$', views.PartsCart, name='PartsCart'),

]