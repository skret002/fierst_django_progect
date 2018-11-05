# -*- coding: utf-8 -*-
from .models import *
from django import forms

CHOICES_TIME = (
        (1, 'Ближайшее время'),
        (2, 'Через час'),
        (3, 'После 14:00'), 
        (4, 'После 17:00'),
        (5, 'После 19:00'),
        (6, 'Завтра до 12:00'), 
        (7, 'Завтра в любое время'),   

    )

class QuestionTV(forms.ModelForm):
    class Meta:
        model = QuestionAboutTV
        exclude = ['']


class OrderingServices(forms.ModelForm):
    time= forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple(attrs={'class':'bootstrap'}),choices=CHOICES_TIME, ),
    class Meta:
        model = OrderingServices
        exclude = ['action']


        widgets = {
            # Укажем для поля favorite_colors нужный нам виджет
            'name': forms.TextInput(attrs={'class':'fb_form form-control cl_bl','placeholder':u'Ваше Имя', 'required':'required'}),
            'phone': forms.TextInput(attrs={'class':'fb_form form-control cl_bl','placeholder':u'Контактыный номер тел.'}),
            'additional_message': forms.Textarea(attrs={'class':'fb_form form-control cl_bl' , 'placeholder':u'Дополнительное сообщение если необходимо'}),
            
        }
