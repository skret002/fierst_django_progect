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
IMAGE_EXT = []

TASK = (
        ('1', 'Обработать и выслать на почту'),
        ('2', 'Распечатать блок фото'),
        ('3', 'Распечатать и выслать на почту'),
    )

class Header(models.Model):
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

class PhotoInfo(models.Model):
    text = models.TextField("Информация", blank=True, null=True)


    def __unicode__(self):
        return "%s" % (self.text,) 

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'


class DocumentCount(models.Model):
    count = models.DecimalField("сколько шт. фото в блоке.", blank=False, null=True, max_digits=2, decimal_places=0)
    
    def __unicode__(self):
        return "%s" % (self.count) 

    class Meta:
        verbose_name = 'шт в БЛОКЕ (не обязательно)'
        verbose_name_plural = 'шт в БЛОКЕ (не обязательно)'

class DocumentOptions(models.Model):
    option = models.CharField("Опции фото",  max_length=500, blank=True, null=False, default=None)

    def __unicode__(self):
        return "%s" % (self.option) 

    class Meta:
        verbose_name = 'Опции фото (не обязательно)'
        verbose_name_plural = 'Опции фото (не обязательно)'

class DocumentFullPrice(models.Model):
    price = models.DecimalField("Цена с печатью блока.", blank=True, null=False, max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "%s" % (self.price) 

    class Meta:
        verbose_name = 'Цена за блок c печатью (не обязательно)'
        verbose_name_plural = 'Цены за блок c печатью (не обязательно)'


class DocumentEditPrice(models.Model):
    price_edit = models.DecimalField("Цена за обработку без печати", null=False, max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "%s" % (self.price_edit) 

    class Meta:
        verbose_name = 'Цена за обработку (не обязательно)'
        verbose_name_plural = 'Цены за обработку (не обязательно)'

class DocumentImagePreview(models.Model):
    image_preview = models.ImageField("Картинка в заголовке", upload_to='photo_doc/', null=False)
    
    def __unicode__(self):
        return "%s" % (self.image_preview) 
    class Meta:
        verbose_name = 'пример блока (не обязательно)'
        verbose_name_plural = 'примеры блока (не обязательно)'

class DocumentType(models.Model):
    name_document = models.CharField("Название документа", max_length=100, blank=True, null=False, default=None)
    count_photo   = models.ForeignKey(DocumentCount,   null=False,  verbose_name= 'кол-во фото в блоке')
    options_photo = models.ForeignKey(DocumentOptions,   null=False,  verbose_name= 'опции фото')
    full_price_photo   = models.ForeignKey(DocumentFullPrice,   null=False,  verbose_name= 'цена с печатью')
    edit_price_photo   = models.ForeignKey(DocumentEditPrice,   null=False,  verbose_name= 'цена за обработку')
    image_preview = models.ForeignKey(DocumentImagePreview,   null=False,  verbose_name= 'пример блока')

    def __unicode__(self):
        return "%s %s %s %s %s %s" % (self.name_document, self.count_photo, self.options_photo, self.full_price_photo, self.edit_price_photo, self.image_preview,) 

    class Meta:
        verbose_name = 'Документ и его параметры'
        verbose_name_plural = 'Документы и его параметры'


class StatusOrder(models.Model):
    status = models.CharField("Cтатус заказа", max_length=35, blank=True, null=False, default=None)

    def __unicode__(self):
        return "%s" % (self.status) 

    class Meta:
        db_table = 'photo_ordering_stat'
        managed = True
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Respondent(models.Model):
    name = models.CharField(max_length=25, null=False, verbose_name='Имя получателя')
    phone = models.CharField(max_length=25, null=False, verbose_name='Тел. Сбербанка')
    namber_bank = models.CharField(max_length=50, null=False, verbose_name='Номер счета в Банке')

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.phone, self.namber_bank, )
    
    class Meta:
        verbose_name = 'Данные Респондента в Банке'
        verbose_name_plural = 'Данные Респондента в Банке'
        

class OrderPhoto(models.Model):
    status = models.CharField(choices=STATUS, max_length=1,  null=True, verbose_name= 'статус заказа')
    name_document = models.CharField("Название документа", max_length=100, blank=True, null=False, default=None)
    name_user= models.CharField("Имя Заказчика", max_length=100, blank=True, null=False, default=None)
    email = models.EmailField("Email", max_length=100, blank=True, null=False, default=None)
    phone_number = models.CharField("Контактный номер",max_length=100, blank=True, null=False,)
    task =MultiSelectField(choices=TASK,max_choices=3,max_length=3)
    you_file = models.FileField("Фотография", upload_to='order_photo_of_doc/', blank=True, null=False)
    comment = models.TextField("Коментарий Заказчика", max_length=1000, blank=True, null=True, default=None)

    def __unicode__(self):
        return "%s %s %s %s %s %s" % (self.status, self.name_document, self.name_user, self.email, self.phone_number,  self.comment) 

    class Meta:
        verbose_name = 'Заказ фото'
        verbose_name_plural = 'Заказы фотографий'