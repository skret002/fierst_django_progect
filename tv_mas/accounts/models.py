# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_or_us = (
            ('Частный клиент', 'Частный клиент'),
            ('Компания', 'Компания'),
    )
    company_or_us_choise = models.CharField("Статус клиента",max_length=14,
                                      choices=company_or_us,
                                      default='Частный клиент')
    tel_number = models.CharField("Номер тел",max_length=24, blank=True)
    tel_number_two = models.CharField("Дополнительный номер тел",max_length=24, blank=True)
    location = models.CharField("Адрес доставки",max_length=100, blank=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()