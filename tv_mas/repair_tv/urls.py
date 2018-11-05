# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from . import views

 
urlpatterns =  [
    url(r'remont_televizorov/$', views.repair_tv_home, name='repair_tv_home'),
    url(r'remont/(?P<brend>[^/]+)/$', views.brend_detail, name='brend_detail'),
    url(r'remont_tv/(?P<brend>[^/]+)/(?P<model>[^/]+)/(?P<service>[^/]+)/$', views.RepairService, name='RepairService'),
  

]