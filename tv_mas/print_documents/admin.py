# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django import forms
# Register your models here.

class OptionDocFieldInline(admin.TabularInline):
    model = OptionDocField
    extra = 0


class PrintDocHeaderAdmin(SummernoteModelAdmin):
    summernote_fields = ('title',)
admin.site.register(PrintDocHeader, PrintDocHeaderAdmin)

class PrintDocInfoAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
admin.site.register(PrintDocInfo, PrintDocInfoAdmin)


@admin.register(StatusOrderDoc,RespondentForDoc)
class DocumentTypeAdmin(admin.ModelAdmin):
    pass



class DocProduktAdmin (admin.ModelAdmin):
    list_display = [field.name for field in DocProdukt._meta.fields]
    #inlines = [FilePhotoInline]

    class Meta:
        model = DocProdukt
admin.site.register(DocProdukt, DocProduktAdmin)


class OrderDocAdmin (admin.ModelAdmin):
    list_display = [field.name for field in OrderDoc._meta.fields]
    inlines = [OptionDocFieldInline ]

    class Meta:
        model = OrderDoc

admin.site.register(OrderDoc, OrderDocAdmin)

