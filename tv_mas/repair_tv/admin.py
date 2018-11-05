# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django import forms
# Register your models here.


class Tv_ModelsInline(admin.TabularInline):
    model = Tv_Models
    extra = 0


class Tv_RepairInline(admin.TabularInline):
    model = Tv_Repair
    extra = 0

   

class Tv_ModelsAdmin(SummernoteModelAdmin):
    summernote_fields = ('info_model',)
    inlines = [Tv_RepairInline]

admin.site.register(Tv_Models, Tv_ModelsAdmin)

class BrendTvAdmin (SummernoteModelAdmin):
    list_display = [field.name for field in BrendTv._meta.fields]
    inlines = [Tv_ModelsInline]
    summernote_fields = ('brend_description',)
    class Meta:
        model = BrendTv

admin.site.register(BrendTv, BrendTvAdmin )

class Tv_RepairAdmin(SummernoteModelAdmin):
    summernote_fields = ('description_service',)
    

admin.site.register(Tv_Repair, Tv_RepairAdmin)


class TextTvHomeAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in TextTvHome._meta.fields]
   
    class Meta:
        model = TextTvHome

admin.site.register(TextTvHome, TextTvHomeAdmin)

admin.site.register(QuestionAboutTV )



def make_unread(modeladmin, request, queryset):
    queryset.update(action=False)
make_unread.short_description = "Отметить группу как не прочитанные"

def make_read(modeladmin, request, queryset):
    queryset.update(action=True)
make_read.short_description = "Отметить группу как ПРОЧИТАННЫЕ" 


class OrderingservicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone' , 'additional_message', 'created' , 'action']
    ordering = ['action']
    actions = [make_read, make_unread]
    list_filter = ('action', 'created')


admin.site.register(OrderingServices,OrderingservicesAdmin)


#admin.site.register(OrderingServices)