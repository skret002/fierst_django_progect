# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save

CHOICES = (
        (1, 'Не для всех ТВ'),
        (2, 'Для всех ТВ'),
    )

CHOICES_TIME = (
        (1, 'Ближайшее время'),
        (2, 'Через час'),
        (3, 'После 14:00'), 
        (4, 'После 17:00'),
        (5, 'После 19:00'),
        (6, 'Завтра до 12:00'), 
        (7, 'Завтра в любое время'),   

    )

CHOICES_ACTION = (
        (False, 'Сообщение не прочитанно'),
        (True, 'Сообщение прочитано '),
    )

# Create your models here.

class BrendTv(models.Model):
    brend = models.CharField("Бренд", max_length=24, blank=True, null=True, default=None)
    brend_logo = models.ImageField("Логотип бренда", upload_to='tv_brend_logo_images/')
    brend_description = models.TextField("Текст-описание в  категории", blank=True, null=True)
    seo_title = models.CharField("SEO Заголовок", max_length=150, blank=True, null=True, default=None)
    seo_description = models.CharField("SEO Описание", max_length=150, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % (self.brend)

    class Meta:
        verbose_name = 'Бренд и модель'
        verbose_name_plural = 'Бренды и модели'

    @property
    def absolute_url(self):
        return reverse('tv_repair:brend_detail', kwargs={'brend': self.brend})




class Tv_Models(models.Model):
    is_brend =  models.ForeignKey(BrendTv, blank=False, null=True,related_name = "tv_models")
    number_tv_model = models.CharField("Модель телевизора", max_length=32, blank=True,)

    
    info_model = models.TextField("характеристики модели", blank=True, null=True)
    model_photo = models.ImageField("Фото модели", upload_to='tv_model_images/', blank=True, null=True)
    model_photo_big= ImageSpecField(source = 'model_photo',
                                            processors=[ResizeToFit(400,)],
                                            format='JPEG',
                                            options={'quality':80})
    model_photo_smoll = ImageSpecField(source = 'model_photo',
                                            processors=[ResizeToFit(200,)],
                                            format='JPEG',
                                            options={'quality':60})

    model_photo_medium = ImageSpecField(source = 'model_photo',
                                            processors=[ResizeToFit(350,)],
                                            format='JPEG',
                                            options={'quality':60})

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % (self.number_tv_model)

    class Meta:
        verbose_name = 'Модель телевизора'
        verbose_name_plural = 'Модели телевизоров'



class Tv_Repair(models.Model):
    service = models.CharField("Услуга",  max_length=150, blank=False, null=True, default=None)
    description_service = models.TextField("Полный текст по неисправности", blank=True, null=True)
    price = models.DecimalField("Цена для 19-24", max_digits=10, decimal_places=2, default=0)
    price2 = models.DecimalField("Цена для 32-37", max_digits=10, decimal_places=2, default=0)
    price3 = models.DecimalField("Цена для 40-42", max_digits=10, decimal_places=2, default=0)
    price4 = models.DecimalField("Цена для 47-52", max_digits=10, decimal_places=2, default=0)
    price5 = models.DecimalField("Цена для 52-55", max_digits=10, decimal_places=2, default=0)
    number_tv_model =  models.ForeignKey(Tv_Models, blank=True, null=True, related_name = "tv_repair")
    kgn = MultiSelectField(choices=CHOICES, max_choices=999, null=True, verbose_name= 'Если услуга для всех тв')
    def __unicode__(self):
        return "№%s | **%s**" % (self.id, self.service)

    class Meta:
        verbose_name = 'Услуга ремонта'
        verbose_name_plural = 'Услуги по ремонту тв'

    @property
    def absolute_url(self):
        return reverse('tv_repair:RepairService', kwargs={'service': self.brend})




class TextTvHome(models.Model):
    title = models.CharField("Зоголовок",  max_length=150, blank=False, null=True, default=None)
    text= models.TextField("ТВ- текст главной", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.title
        

    class Meta:
        verbose_name = 'Ремонт ТВ- текст главной'
        verbose_name_plural = 'Ремонт ТВ- текст главной'


class QuestionAboutTV(models.Model):
    you_name = models.CharField("Имя", max_length=24)
    phone = models.CharField("Номер телефона", max_length=18)
    you_email = models.EmailField("EMAIL", blank=True, null=True)
    tv_brend = models.CharField("Марка ТВ (Бренд)", max_length=24, blank=True, null=True)
    tv_model = models.CharField("Модель ТВ ", max_length=24, blank=True, null=True)
    you_question = models.TextField("Вопрос мастерам", max_length=300)
    you_file = models.FileField("Фотография если необходимо", upload_to='question_about_tV/', blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.you_name

    class Meta:
        verbose_name = 'Вопрос по ТВ (Нет в нашей базе)'
        verbose_name_plural = 'Вопросы по ТВ (Нет в нашей базе)'


class OrderingServices(models.Model):
    action              = models.BooleanField(choices=CHOICES_ACTION, max_length=1, default = False, null=False, blank=True, verbose_name= 'Прочитано или не прочитано сообщение')
    name                = models.CharField("Имя", max_length=24, blank=True, null=False)
    phone               = models.CharField("Номер телефона", max_length=18, blank=True, null=False)
    time                = MultiSelectField(choices=CHOICES_TIME, max_choices=3, blank=True, null=False, verbose_name="Удобное время звонка")
    brend_tv            = models.CharField("Марка ТВ", max_length=34, blank=True, null=False)
    model_tv            = models.CharField("Модель ТВ", max_length=34, blank=True, null=False)
    crash               = models.CharField("Какая проблемма", max_length=34, blank=True, null=False)
    additional_message  = models.TextField("Дополнительное сообщение", max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __unicode__(self):
        return " ***%s***   | %s | %s | %s | %s " % (self.action, self.name, self.phone, self.model_tv, self.crash )

    class Meta:
        verbose_name = 'Заказ на РЕМОНТ'
        verbose_name_plural = 'Заказ на РЕМОНТ'

#def ordering_services_post_save(sender, **kwargs):
#
#    objects = OrderingServices.objects.filter(action='1')
#    print(objects, "POST_SIGNAL_OK")
#    for i in objects:
#        if i.action == '1':
#            i.action = 'НЕ ПРОЧИТАНО'
#            i.save()
#    objects_too = OrderingServices.objects.filter(action='2')
#    for i in objects_too:
#        if i.action == '2':
#            i.action = 'уже прочитано'
#            i.save()    
#
#
#post_save.connect(ordering_services_post_save, sender=OrderingServices)