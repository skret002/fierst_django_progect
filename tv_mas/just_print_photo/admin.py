# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django import forms
# Register your models here.

class OptionPhotoFieldInline(admin.TabularInline):
    model = OptionPhotoField
    extra = 0


class PrintPhotoHeaderAdmin(SummernoteModelAdmin):
    summernote_fields = ('title',)
admin.site.register(PrintPhotoHeader, PrintPhotoHeaderAdmin)

class PrintPhotoInfoAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
admin.site.register(PrintPhotoInfo, PrintPhotoInfoAdmin)


@admin.register(StatusOrderPhoto,RespondentForPhoto)
class DocumentTypeAdmin(admin.ModelAdmin):
    pass



class PhotoProduktAdmin (admin.ModelAdmin):
    list_display = [field.name for field in PhotoProdukt._meta.fields]
    #inlines = [FilePhotoInline]

    class Meta:
        model = PhotoProdukt
admin.site.register(PhotoProdukt, PhotoProduktAdmin)


class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [OptionPhotoFieldInline ]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

