# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django import forms
# Register your models here.
#admin.site.register(DocumentCount)
#admin.site.register(DocumentType)
#admin.site.register(Header)



class HeaderAdmin(SummernoteModelAdmin):
    summernote_fields = ('title',)
#    inlines = [Header]

admin.site.register(Header, HeaderAdmin)

class PhotoInfoAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
#    inlines = [Header]

admin.site.register(PhotoInfo, PhotoInfoAdmin)

@admin.register(DocumentCount, DocumentOptions, DocumentFullPrice, DocumentEditPrice,DocumentImagePreview,StatusOrder,Respondent)
class DocumentTypeAdmin(admin.ModelAdmin):
    pass

class OrderPhotoAdmin (admin.ModelAdmin):
    list_display = [field.name for field in OrderPhoto._meta.fields]

    class Meta:
        model = OrderPhoto

admin.site.register(OrderPhoto, OrderPhotoAdmin)

class DocumentTypeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in DocumentType._meta.fields]

    class Meta:
        model = DocumentType

admin.site.register(DocumentType, DocumentTypeAdmin)