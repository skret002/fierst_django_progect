# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Orders
from django import forms


class Orders(forms.ModelForm):
    class Meta:
        model = Orders
        exclude = ['payment', 'final_status_order', 'read_unread','read_unread','final_status_order','payment','created','updated']


    error_css_class = 'error'
    required_css_class = 'required'


    def __init__(self, *args, **kwargs):
        super(Orders, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-sm form_order'
            self.fields['name'].widget.attrs['id'] = 'formGroupExampleInput'
            self.fields['phone_number'].widget.attrs['placeholder'] = '+7xxxxxxxxxx *обязательно с +7'
            self.fields['location'].widget.attrs['placeholder'] = 'Можно не указывать, менеджер уточнит!'
            self.fields['order_option'].widget.attrs['class'] = 'custom-select '
            self.fields['order_day'].widget.attrs['class'] = 'custom-select'
            self.fields['order_time'].widget.attrs['class'] = 'custom-select'
            #self.fields['order_problem_name'].widget.attrs['class'] = 'custom-select'

    def as_div(self):
        
        return self._html_output(
            #normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            normal_row = u'<div class = "form_order"%(html_class_attr)s>%(label)s%(field)s %(help_text)s </div>',
            error_row = u'<div class="error">%s</div>',
            row_ender = '</div>',
            help_text_html = u'<div class="help-text">%s</div>',
            errors_on_separate_row = False)
