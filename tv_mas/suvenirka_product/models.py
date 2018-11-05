# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Product(models.Model):
    name = models.CharField("название", max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField("цена", max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField("скидка", default=0)
    size = models.CharField("размер", max_length=64, blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    short_description = models.TextField("короткое описание", blank=True, null=True, default=None)
    description = models.TextField("полное описание", blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ["price"]

class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ["product__price"]
 

class ColorField(models.Model):
    product_color = models.ForeignKey(Product, blank=True, null=True)
    name = models.CharField("название цвета", max_length=16, default="Белый")
    color_img = models.ImageField("цвет товара (фото)", upload_to='products_images/', blank=True, null=True, default= "None" )

    def __unicode__(self):
            return "%s" % (self.name)

    class Meta:
        verbose_name = 'цвет товара(img)'
        verbose_name_plural = 'цвет товаров(img)'


class IssuesProdukt(models.Model):
    issues_url = models.URLField("Страница с которой пришел вопрос")
    you_name = models.CharField("Имя",max_length=24, blank=True, null=True, default=None)
    you_phone = models.CharField("Телефон",max_length=18, blank=True, null=True, default=None)
    you_question = models.CharField("Вопрос по товару",max_length=200, blank=True, null=True, default=None)

    def __unicode__(self):
        return "%s" % (self.you_name)

    class Meta:
        verbose_name = 'Вопрос по товару в сувенирки'
        verbose_name_plural = 'Вопрос по товару в сувенирки'


class Description_Category(models.Model):
    page = models.ForeignKey(ProductCategory, blank=True, null=True) 
    text= models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.page.name
        

    class Meta:
        verbose_name = 'Текст в категории товара'
        verbose_name_plural = 'Тексты в категориях товара'

