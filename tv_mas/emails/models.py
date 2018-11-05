# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EmailType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
            return "%s" % (self.name)


    class Meta:
        verbose_name = 'Тип Имейла'
        verbose_name_plural = 'Типы Имейлов'

class EmailSendingFact(models.Model):
    type = models.ForeignKey(EmailType)
    order = models.ForeignKey("suvenirka_order.Order", blank=True, null=True, default=None )
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.type.name


    class Meta:
        verbose_name = 'Отправленный имейл'
        verbose_name_plural = 'Отправленные имейлы'