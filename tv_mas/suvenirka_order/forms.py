# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import *
from django.forms.formsets import formset_factory

class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    address_dostavka = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    comment_zakaz  = forms.CharField(required=False, widget=forms.Textarea)
    image = forms.FileField(label='Загразка фото',required=False)
    image_title = forms.CharField(required=False)
#class ProfileImageForm(forms.Form):
#   image = forms.FileField(label='Select a profile Image')
#
#class UploadFileForm(forms.Form):
#    image = forms.FileField(label='Select a profile Image')