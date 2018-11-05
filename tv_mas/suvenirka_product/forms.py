# -*- coding: utf-8 -*-
from .models import *
from django import forms



class PriceFilter(forms.Form):
    min_price = forms.IntegerField(label="от", required=False, initial='0')
    max_price = forms.IntegerField(label="до", required=False)



class QuestionProdukt(forms.ModelForm):
    class Meta:
        model = IssuesProdukt
        exclude = ["issues_url"]

        widgets = {
        'you_name':forms.TextInput(attrs={'class':'fb_form form-control', 'cols':10, 'placeholder':'Ваше имя'}),
        'issues_url':forms.URLField(),
        'you_phone':forms.TextInput(attrs={'class':'fb_form form-control','placeholder':'Контактный телефон'}),
        'you_question': forms.Textarea(attrs={'class':'fb_form form-control','cols':40,'placeholder':'Напишите свой вопрос'})
        }
