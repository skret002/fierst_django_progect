# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib import admin
from django_summernote.widgets import SummernoteWidget   

from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django import forms

# Register your models here.
#admin.site.register(SmartfonBrend)
#admin.site.register(SmartfonModels)
#admin.site.register(Spare_Part)
#admin.site.register(PriceService)
#admin.site.register(ActionProblem)
#admin.site.register(QualityPart)
#admin.site.register(ChoicesAvailable)
#admin.site.register(RepairPlace)
#admin.site.register(Orders)


class NotebookBrendAdmin (admin.ModelAdmin):
    list_display = [field.name for field in NotebookBrend._meta.fields]
    class Meta:
        model = NotebookBrend
admin.site.register(NotebookBrend, NotebookBrendAdmin)

class NotebookModelsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in NotebookModels._meta.fields]
    class Meta:
        model = NotebookModels
admin.site.register(NotebookModels, NotebookModelsAdmin)


class Spare_PartAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Spare_Part._meta.fields]
    list_filter = ('notebookmodels__model', 'action_problem__name_service')
    search_fields = ['notebookmodels__model', 'name_service','description_service',]

    class Meta:
        model = Spare_Part 
admin.site.register(Spare_Part, Spare_PartAdmin)

class PriceServiceAdmin (admin.ModelAdmin):
    list_display = [field.name for field in PriceService._meta.fields]
    class Meta:
        model = PriceService
admin.site.register(PriceService, PriceServiceAdmin)

class ActionProblemAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ActionProblem._meta.fields]
    class Meta:
        model = ActionProblem
admin.site.register(ActionProblem, ActionProblemAdmin)

class QualityPartAdmin (admin.ModelAdmin):
    list_display = [field.name for field in QualityPart._meta.fields]
    class Meta:
        model = QualityPart
admin.site.register(QualityPart, QualityPartAdmin)


class ChoicesAvailableAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ChoicesAvailable._meta.fields]
    class Meta:
        model = ChoicesAvailable
admin.site.register(ChoicesAvailable, ChoicesAvailableAdmin)


class RepairPlaceAdmin (admin.ModelAdmin):
    list_display = [field.name for field in RepairPlace._meta.fields]
    class Meta:
        model = RepairPlace
admin.site.register(RepairPlace, RepairPlaceAdmin)


class OrdersAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Orders._meta.fields]
    class Meta:
        model = Orders
admin.site.register(Orders, OrdersAdmin)


class OutServiceAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in OutService._meta.fields]
    summernote_fields = ('text_out_service',)
   
    class Meta:
        model = OutService
admin.site.register(OutService, OutServiceAdmin)


class DopInfoServiceAdmin(SummernoteModelAdmin):
    list_display = [field.name for field in DopInfoService._meta.fields]
    summernote_fields = ('client_sc','info_sc','info_prise')
   
    class Meta:
        model = DopInfoService
admin.site.register(DopInfoService, DopInfoServiceAdmin)