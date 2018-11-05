# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
# Create your models here.


class CartridgePrinters(models.Model):
    brend = models.CharField("Бренд", max_length=32, blank=True, null=True, default=None)
    model_printer = models.CharField("Модели Принтеров", max_length=50, blank=True, null=False, default=None)
    number_cartridge = models.CharField("Номер Картриджа", max_length=50, blank=True, null=True, default=None)
    refill_cartridge = models.DecimalField("Заправка картриджа", max_digits=8, decimal_places=2, blank=True,  null=True)
    replacing_chip = models.DecimalField("Замена чипа", max_digits=8, decimal_places=2, blank=True,  null=True)
    replacing_printing_drum  = models.DecimalField("Замена фотовала", max_digits=8, decimal_places=2, blank=True,  null=True)
    replacing_magnetic  = models.DecimalField("Замена Магнитного Вала", max_digits=8, decimal_places=2, blank=True,  null=True)


    def __unicode__(self):
        return "%s %s %s %s %s %s %s" % (self.brend, self.model_printer, self.number_cartridge, self.refill_cartridge,self.replacing_chip,
                                            self.replacing_printing_drum, self.replacing_magnetic,)

    class Meta:
        db_table = 'CartridgeCase'
        managed = True
        verbose_name = 'Картридж и принтер'
        verbose_name_plural = 'Картриджи и принтеры'

    @property
    def absolute_url(self):
        return reverse('refcartridges:devaice_search', kwargs={'number': self.number_cartridge})