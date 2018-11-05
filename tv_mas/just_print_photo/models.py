# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
#from just_print_photo.views import part_file_url
# Create your models here.


COUNT_PHOTO = []
OPTION_PHOTO = []
FULL_PRICE_PHOTO =[]
EDIT_PRICE_PHOTO =[]
STATUS =(
        ('1', 'В обработке'),
        ('2', 'Обработан'),
        ('3', 'Выдан'),
    )
MARGIN = (
        ('0', 'С полями'),
        ('1', 'Без полей'),
        ('2', 'На усмотрение'),
)
SELECT_TIME=(
        ('0', 'Как можно быстрее'),
        ('1', 'В течении дня'),
        ('2', 'Не срочно'),
        ('3', 'Заберу после завтра'),
        ('4', 'Заберу на недели'),

    )
IMAGE_EXT = []

TASK = (
        ('0', 'НЕТ'),
        ('1', 'ДА'),

    )
FILE = []


#print(upload_url())

class PrintPhotoHeader(models.Model):
    title = models.CharField("Текст в заголовке",  max_length=1000, blank=True, null=True, default=None)
    image_header = models.ImageField("Картинка в заголовке", upload_to='photo_doc/',blank=True, null=True)
    image_header_hd= ImageSpecField(source = 'image_header',
                                            processors=[ResizeToFit(1920,400)],
                                            format='JPEG',
                                            options={'quality':90})
    image_header_notebook = ImageSpecField(source = 'image_header',
                                            processors=[ResizeToFit(1366, 400)],
                                            format='JPEG',
                                            options={'quality':90})

    image_header_medium = ImageSpecField(source = 'image_header',
                                            processors=[ResizeToFit(1280,400)],
                                            format='JPEG',
                                            options={'quality':90})
    image_header_smoll= ImageSpecField(source = 'image_header',
                                            processors=[ResizeToFit(768,)],
                                            format='JPEG',
                                            options={'quality':90})
    
    def __unicode__(self):
        return "%s   %s" % (self.title, self.image_header) 

    class Meta:
        verbose_name = 'Заголовок в Фото на документы'
        verbose_name_plural = 'Заголовоки в Фото на документы'

class PrintPhotoInfo(models.Model):
    text = models.TextField("Информация", blank=True, null=True)


    def __unicode__(self):
        return "%s" % (self.text,) 

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'



class PhotoProdukt(models.Model):
    format_photo = models.CharField("Формат фотографии", max_length=10, blank=True, null=False, default=None)
    type_paper   = models.CharField("Тип бумаги", max_length=100, blank=True, null=False, default=None)
    price_smollshipment = models.DecimalField("Цена до 20шт", max_digits=5, decimal_places=2,  null=False)
    price_medium_shipment = models.DecimalField("Цена от 20 до 100шт", max_digits=5, decimal_places=2,  null=False) 
    price_big_shipment = models.DecimalField("Цена от 20 до 100шт", max_digits=5, decimal_places=2,  null=False) 
    def __unicode__(self):
        return "%s %s %s %s %s " % (self.format_photo, self.type_paper, self.price_smollshipment, self.price_medium_shipment, self.price_big_shipment,) 

    class Meta:
        verbose_name = 'Формат фотографии и  параметры'
        verbose_name_plural = 'Форматы фотографии и  параметры'


class StatusOrderPhoto(models.Model):
    status = models.CharField("Cтатус заказа", max_length=35, blank=True, null=False, default=None)

    def __unicode__(self):
        return "%s" % (self.status) 

    class Meta:
        db_table = 'photo_order'
        managed = True
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class RespondentForPhoto(models.Model):
    name = models.CharField(max_length=25, null=False, verbose_name='Имя получателя')
    phone = models.CharField(max_length=25, null=False, verbose_name='Тел. Сбербанка')
    namber_bank = models.CharField(max_length=50, null=False, verbose_name='Номер счета в Банке')

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.phone, self.namber_bank, )
    
    class Meta:
        verbose_name = 'Данные Респондента в Банке'
        verbose_name_plural = 'Данные Респондента в Банке'

class Customer(models.Model):
    name_user = models.CharField("Имя Заказчика", max_length=100, null=False,)            
    phone_number = models.CharField("Контактный номер", max_length=100,)
    email = models.EmailField("Email", max_length=100, null=False,)
    
    def __unicode__(self):
        return "%s %s %s" % (self.name_user, self.phone_number, self.email,) 

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'    


class NumberOrder(models.Model):
    number_order = models.CharField(max_length=6,  null=False, verbose_name= 'Номер Заказа')

    def __unicode__(self):
        return "%s" % (self.number_order) 

    class Meta:
        verbose_name = 'Номер Заказа'
        verbose_name_plural = 'Номера Заказов'


class FilePhoto( models.Model):
    options = models.ForeignKey('OptionPhotoField', related_name='OptionPhotoField', verbose_name= "Опция Фотографии")

    def __unicode__(self):
        return "%s" % (self.options) 

    class Meta:
        verbose_name = 'фотографии'
        verbose_name_plural = 'фотографии'  

class Order(models.Model):
    number_orders = models.ForeignKey('NumberOrder', related_name='number', verbose_name= "Номер Заказа")
    status = models.CharField(choices=STATUS, max_length=1,  null=True, verbose_name= 'статус заказа')
    user = models.ForeignKey('Customer', related_name='user_photos', verbose_name= "Заказчик")
    task_call = models.CharField(choices=TASK, max_length=1, default='0', verbose_name="Нужен звонок клиенту")
    count_price= models.DecimalField("Всего к оплате", max_digits=9, decimal_places=0,  null=False)
    comment = models.TextField("Коментарий Заказчика", max_length=1000, blank=True, null=True, default=None)

    def __unicode__(self):
            return "%s %s %s %s " % (self.number_orders, self.status, self.user,self.comment,) 

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OptionPhotoField(models.Model):
    files = models.FileField("Фотография", upload_to='order__print_photo/', blank=True, null=False)
    order = models.ForeignKey('Order', related_name='Order', verbose_name= "Заказ")
    count_photo = models.CharField("кол-во копий", max_length=3, null=False, default=None)
    photo_product= models.ForeignKey('PhotoProdukt', related_name='id_product')
    with_margin = models.CharField("C полями или без", choices=MARGIN,   max_length=1,  null=True)
    time_take = models.CharField(choices=SELECT_TIME, max_length=1,  null=True, verbose_name= 'когда заберут')


    def __unicode__(self):
        return "%s %s %s %s %s %s " % (self.files, self.order, self.count_photo, self.photo_product, self.with_margin, self.time_take,) 

    class Meta:
        verbose_name = 'опции фотографий'
        verbose_name_plural = 'опции фотографий'  