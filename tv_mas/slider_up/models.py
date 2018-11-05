# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.



class Slider_up(models.Model):
    class Meta:
        verbose_name = 'Тексты к слайдеру'
    name_buttom = models.CharField(max_length=24, blank=True, null=True, default=None, verbose_name ='текст в кнопке')
    slide_text = models.CharField(max_length = 200, blank = True, verbose_name ='описание в слайде')
    is_active = models.BooleanField(default=True)
        
    def __unicode__(self):
        return "текст к слайдеру %s " %(self.name_buttom)

class Slider_image(models.Model):
    class Meta:
        verbose_name = 'Картинки в слайдереру 1366'
    image_to_slide = models.ForeignKey(Slider_up, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/', blank = True, verbose_name ='картинки HD')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
       
    def __unicode__(self):
        return "%s" % self.id

class Slider_image_tablet(models.Model):
    class Meta:
        verbose_name = 'Картинки в слайдереру 768'
    image_to_slide = models.ForeignKey(Slider_up, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/', blank = True, verbose_name ='картинки HD')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
       
    def __unicode__(self):
        return "%s" % self.id

class Slider_image_mobile(models.Model):
    class Meta:
        verbose_name = 'Картинки в слайдереру  360'
    image_to_slide = models.ForeignKey(Slider_up, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/', blank = True, verbose_name ='картинки HD')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
       
    def __unicode__(self):
        return "%s" % self.id


class Description_suvenirka(models.Model):
    class Meta:
        verbose_name = 'SEO для suvenirka/suvenirka.html'
    
    title = models.CharField(max_length = 80, blank = True, verbose_name ='TITLE для suvenirka.html')
    description = models.CharField(max_length = 200, blank = True, verbose_name ='Description для suvenirka.html')
    keywords = models.CharField(max_length = 120, blank = True, verbose_name ='keywords для suvenirka.html')
    
    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'SEO для suvenirka/suvenirka.html'
        verbose_name_plural = 'SEO для suvenirka/suvenirka.html'