# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
#from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CartridgePrintersResource(resources.ModelResource):
    brend = Field(attribute='brend', column_name='БРЕНД')
    model_printer = Field(attribute='model_printer', column_name='МОДЕЛИ ПРИНТЕРОВ')
    number_cartridge = Field(attribute='number_cartridge', column_name='НОМЕР КАРТРИДЖА')
    refill_cartridge = Field(attribute='refill_cartridge', column_name='ЗАПРАВКА КАРТРИДЖА')
    replacing_chip = Field(attribute='replacing_chip', column_name='ЗАМЕНА ЧИПА')
    replacing_printing_drum = Field(attribute='brend', column_name='ЗАМЕНА ФОТОВАЛА')
    replacing_magnetic = Field(attribute='replacing_magnetic', column_name='ЗАМЕНА МАГНИТНОГО ВАЛА')

    class Meta:
        model = CartridgePrinters


class CartridgePrintersAdmin(ImportExportActionModelAdmin):
    resource_class = CartridgePrintersResource
    list_display = [field.name for field in CartridgePrinters._meta.fields]

admin.site.register(CartridgePrinters, CartridgePrintersAdmin)

