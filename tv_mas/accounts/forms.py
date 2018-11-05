# -*- coding: utf-8 -*-
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
        'first_name':forms.TextInput(attrs={'class':'fb_form form-control', 'cols':10}),
        'last_name':forms.TextInput(attrs={'class':'fb_form form-control','cols':20}),
        'email': forms.TextInput(attrs={'class':'fb_form form-control'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]

        widgets = {
        'company_or_us_choise':forms.Select(attrs={'class':'fb_form form-control', 'id':'exampleFormControlSelect1', 'cols':10}),
        'tel_number':forms.TextInput(attrs={'class':'fb_form form-control','placeholder':'Контактный телефон'}),
        'tel_number_two':forms.TextInput(attrs={'class':'fb_form form-control','placeholder':'Дополнительный номер тел.'}),
        'location': forms.Textarea(attrs={'class':'fb_form form-control','cols':40,'placeholder':'Адрес доставки'})
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control register_form form-control form-control-sm reg_p', 'placeholder':u'Придумайте логин'}),
        'first_name':forms.TextInput(attrs={'class':'form-control register_form form-control form-control-sm reg_p','placeholder':u'Ваше Имя '}),
        'last_name':forms.TextInput(attrs={'class':'form-control register_form form-control form-control-sm reg_p','placeholder':u'Фамилия'}),
        'email': forms.Textarea(attrs={'class':'form-control register_form form-control form-control-sm reg_p','placeholder':'EMAIL'}),
        'password1': forms.PasswordInput(attrs={'class':' form-control register_form form-control form-control-sm reg_p','placeholder':u'пароль'}),
        'password2': forms.PasswordInput(attrs={'class':'form-control register_form form-control form-control-sm reg_p','placeholder':u'Повторите пароль'}),
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user