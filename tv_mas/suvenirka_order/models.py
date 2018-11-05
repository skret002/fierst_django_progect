# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.db.models.signals import post_save
from suvenirka_product.models import ColorField, Product

from django.contrib.auth import authenticate, login

#from utils.main import disable_for_loaddata

# Create your models here.

class Status(models.Model):

    name = models.TextField(max_length=24)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "Статус %s" % (self.name)


    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'
  

class Userimage(models.Model):
    image = models.FileField(upload_to='user_image/')
    def __unicode__(self):
        return  "фото %s"  % (self.id)

    class Meta:
        verbose_name = 'фото к заказу СУВЕНИРКА'
        verbose_name_plural = 'фотографии к заказу СУВЕНИРКА'


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status =  models.ForeignKey(Status, default=10)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
   

    def __unicode__(self):
        if self.status: 
            return "%s" % (self.status.name) 
        else: return "%s" % (self.id)
        #return "Заказ %s " % (self.id)



    class Meta:
        verbose_name = 'Заказ СУВЕНИРКА'
        verbose_name_plural = 'Заказы СУВЕНИРКА'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
    




class ProductInOrder(models.Model):
    us_image = models.ForeignKey(Userimage )
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    color_check = models.CharField(max_length=24, blank=True, null=True, default=None)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе СУВЕНИРКА'
        verbose_name_plural = 'Товары в заказе СУВЕНИРКА'


    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item
        
        super(ProductInOrder, self).save(*args, **kwargs)


#@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)



class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=256, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    color_check = models.CharField(max_length=24, blank=True, null=True, default=None)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % (self.product.name)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item
        super(ProductInBasket, self).save(*args, **kwargs)

