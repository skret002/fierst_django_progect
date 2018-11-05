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
# MyClass


ORDER_OPTION = (
        ('0', 'Не нужно'),
        ('1', 'Вызвать мастера'),
        ('2', 'Вызвать курьера'),
    )

ORDER_DAY_OPTION = (
        ('0', 'ПН'),('1', 'ВТ'),('2', 'СР'),('3', 'ЧТ'),('4', 'ПТ'),('5', 'СБ'),('6', 'ВС'),

    )
ORDER_TIME_OPTION = (
        ('1', '8:00'),('2', '8:30'),('3', '9:00'),('4', '9:30'),('5', '10:00'),('6', '10:30'),('7', '11:00'),('8', '11:30'),
        ('9', '12:00'),('10', '12:30'),('11', '13:00'),('12', '13:30'),('13', '14:00'),('14', '14:30'),('15', '15:00'),
        ('16', '15:30'),('17', '16:00'),('18', '16:30'),('19', '17:00'),('20', '17:30'),('21', '18:00'),('22', '18:30'),
        ('23', '19:00'),('24', '19:30'),('25', '20:00'),('26', '20:30'),('27', '21:00'),
    )

READ_UNREAD = (
        ('False', 'Не прочитано'),
        ('True',  'Прочитано'),

    )
MANAGE_ACTION = (
        ('0', 'Отправлен курьер'),
        ('1', 'Отправлен мастер'),
        ('2', 'Заявка продана другому СЦ'),
    )

class NotebookBrend(models.Model):
    brend = models.CharField("Бренд", max_length=24, blank=True, null=True, default=None)
    image_brend = models.ImageField("Логотип бренда", upload_to='smarfon_brend/',blank=True, null=True)
    description_brend = models.TextField("Описание Бренда", max_length=1000, blank=True, null=True, default=None)
    image_brend_big= ImageSpecField(source = 'image_brend',
                                            processors=[ResizeToFit(400,)],
                                            format='JPEG',
                                            options={'quality':80})
    image_brend_smoll = ImageSpecField(source = 'image_brend',
                                            processors=[ResizeToFit(200,)],
                                            format='JPEG',
                                            options={'quality':60})

    image_brend_medium = ImageSpecField(source = 'image_brend',
                                            processors=[ResizeToFit(350,)],
                                            format='JPEG',
                                            options={'quality':60})
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return "%s" % (self.brend)

    class Meta:
        verbose_name = 'Бренд ноутбука'
        verbose_name_plural = 'Бренды и ноутбуков'

    @property
    def absolute_url(self):
        return reverse('notebook:notebook_home_and_search', kwargs={'brend': self.brend})



class NotebookModels(models.Model):
    brend_key = models.ForeignKey(NotebookBrend, blank=False, null=True, related_name = "notebook_brend")
    model = models.CharField("Модель", max_length=24, blank=True, null=True, default=None)
    description_models = models.TextField("Описание модели", max_length=1000, blank=True, null=True, default=None)
    image_models = models.ImageField("Фото модели", upload_to='smarfon_model/',blank=True, null=True)    
    image_brend_big= ImageSpecField(source = 'image_models',
                                            processors=[ResizeToFit(400,)],
                                            format='JPEG',
                                            options={'quality':80})
    image_brend_smoll = ImageSpecField(source = 'image_models',
                                            processors=[ResizeToFit(200,)],
                                            format='JPEG',
                                            options={'quality':60})

    image_brend_medium = ImageSpecField(source = 'image_models',
                                            processors=[ResizeToFit(350,)],
                                            format='JPEG',
                                            options={'quality':60})
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        
        
    def __unicode__(self):
        return "%s" % (self.model)

    class Meta:
        verbose_name = 'Модель ноутбука'
        verbose_name_plural = 'Модели и ноутбука'

    @property
    def absolute_url(self):
        return reverse('notebook:notebook_home_and_search', kwargs={'model': self.model})



class PriceService(models.Model):
    shipping_cost   = models.DecimalField("Цена доставки", max_digits=5, decimal_places=2, blank=True, null=True, default=0)
    #******************************НАЦЕНКА НА ЗЧ*****************************************************
    part_price_zero      = models.DecimalField("% увеличение цены ЗЧ: Если до 100р", blank=True, null=True, max_digits=7, decimal_places=2)
    part_price_one       = models.DecimalField("% увеличение цены ЗЧ: Если до 350р", blank=True, null=True, max_digits=7, decimal_places=2)
    part_price_two       = models.DecimalField("% увеличение цены ЗЧ: Если 350-700р", blank=True, null=True, max_digits=7, decimal_places=2)
    part_price_three     = models.DecimalField("% увеличение цены ЗЧ: Если 700-2000р", blank=True, null=True, max_digits=7, decimal_places=2)
    part_price_four      = models.DecimalField("% увеличение цены ЗЧ: Если 2000-5000р", blank=True, null=True, max_digits=7, decimal_places=2)
    part_price_five      = models.DecimalField("% увеличение цены ЗЧ: Если > 5000р", blank=True, null=True, max_digits=7, decimal_places=2)

    #******************************СТОИМОСТЬ *****************************************************
    price_one       = models.DecimalField("Цена Работ - Если цена ЗЧ до 1500р", blank=True, null=True, max_digits=7, decimal_places=2)
    price_two       = models.DecimalField("Цена Работ - Если цена ЗЧ 1500-3500р", blank=True, null=True, max_digits=7, decimal_places=2)
    price_three     = models.DecimalField("Цена Работ - Если цена ЗЧ 3500р-7000р", blank=True, null=True, max_digits=7, decimal_places=2)
    price_four      = models.DecimalField("Цена Работ - Если цена ЗЧ 7000-10000р", blank=True, null=True, max_digits=7, decimal_places=2)
    price_five      = models.DecimalField("Цена Работ - Если цена ЗЧ > 10000р", blank=True, null=True, max_digits=7, decimal_places=2)
    
    def __unicode__(self):
        return "%s" % (self.shipping_cost) 


    class Meta:
        verbose_name = 'Стоимость работ и наценка на ЗЧ'
        verbose_name_plural = 'Стоимости работ и наценка на ЗЧ'



class ActionProblem(models.Model):
    name_service    = models.CharField("Категория проблем", max_length=100, blank=True, null=False, default=None)

    def __unicode__(self):
        return "%s   %s" % (self.id, self.name_service) 


    class Meta:
        verbose_name = 'Категория проблем'
        verbose_name_plural = 'Категории проблем'

class RepairPlace(models.Model):
    place    = models.CharField("Где возможен ремонт", max_length=24, blank=True, null=False, default=None)

    def __unicode__(self):
        return "%s   %s" % (self.id, self.place) 


    class Meta:
        verbose_name = 'Где возможен ремонт'
        verbose_name_plural = 'Где возможны ремонты'

class QualityPart(models.Model):
    quality    = models.CharField("Качество запчастей", max_length=100, blank=True, null=False, default=None)

    def __unicode__(self):
        return "%s   %s" % (self.id, self.quality) 


    class Meta:
        verbose_name = 'Качество запчастей'
        verbose_name_plural = 'Качество запчастей'


class ChoicesAvailable(models.Model):
    available    = models.CharField("Наличие ЗЧ", max_length=50, blank=True, null=False, default=None)

    def __unicode__(self):
        return "%s   %s" % (self.id, self.available) 


    class Meta:
        verbose_name = 'Наличие ЗЧ'
        verbose_name_plural = 'Наличие ЗЧ'



class Spare_Part(models.Model):
    notebookmodels  = models.ForeignKey(NotebookModels, blank=True, null=True, related_name = "notebook_models")
    action_problem  = models.ForeignKey(ActionProblem,  blank=True, null=True, verbose_name="Категория проблем")
    name_service    = models.CharField("Название Услуги",  max_length=200, blank=True, null=True, default=None) #unique=True,
    available_part  = models.ForeignKey(ChoicesAvailable, blank=True, null=True, related_name = "choices_available", verbose_name= 'Наличие ЗЧ')
    quality_part    = models.ForeignKey(QualityPart, blank=True, null=True, related_name = "quality_part", verbose_name= 'Качество ЗЧ')
    repair_place    = models.ForeignKey(RepairPlace, blank=True, null=True, related_name = "repair_place", verbose_name= 'Где возможен ремонт')
    popular_service = models.BooleanField("Включить в популярные услуги", default=None)
    autocheck       = models.BooleanField("Включить автопросчет цены", default=True)
    sale            = models.BooleanField("Товар в акции", default=False)
    price_sale      = models.DecimalField("Скидка по акции в руб.", blank=True, null=True, max_digits=7, decimal_places=2)
    all_notebook    = models.BooleanField("Включить услугу для всех моделей", default=False)
    base_prise      = models.DecimalField("Реальная цена ЗЧ", blank=True, null=True, max_digits=7, decimal_places=2)
    full_prise      = models.DecimalField("Окончательная цена", blank=True, null=True, max_digits=7, decimal_places=2) 

    time_on_repairs = models.CharField("Время на ремонт", max_length=60, blank=True, null=True, default=None)
    description_service = models.TextField("Описание Услуги", max_length=1000, blank=True, null=True, default=None)
    
    image_part_base = models.ImageField("Фото Запчасти", upload_to='smarfon_part/',blank=True, null=True)    
    image_part_base_big= ImageSpecField(source = 'image_part_base',
                                            processors=[ResizeToFit(400,)],
                                            format='JPEG',
                                            options={'quality':50})
    image_part_base_smoll = ImageSpecField(source = 'image_part_base',
                                            processors=[ResizeToFit(200,)],
                                            format='JPEG',
                                            options={'quality':50})

    image_part_base_medium = ImageSpecField(source = 'image_part_base',
                                            processors=[ResizeToFit(350,)],
                                            format='JPEG',
                                            options={'quality':50})


    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s**     **%s     **%s" % (self.notebookmodels, self.popular_service, self.name_service) 

    class Meta:
        verbose_name = 'Запчать  ноутбука'
        verbose_name_plural = 'Запчасти ноутбука'


    @property
    def sum(self):
        # наценка если стоимость ЗЧ = base_prise
        shipping_cost = PriceService.objects.all()[0].shipping_cost  # доставка
        part_price_zero = PriceService.objects.all()[0].part_price_zero
        part_price_one  = PriceService.objects.all()[0].part_price_one
        part_price_two  = PriceService.objects.all()[0].part_price_two
        part_price_three = PriceService.objects.all()[0].part_price_three
        part_price_four  = PriceService.objects.all()[0].part_price_four
        part_price_five  = PriceService.objects.all()[0].part_price_five

        # Стоимость работ если  стоимость ЗЧ <>
        price_one  = PriceService.objects.all()[0].price_one
        price_two  = PriceService.objects.all()[0].price_two
        price_three  = PriceService.objects.all()[0].price_three
        price_four  = PriceService.objects.all()[0].price_four
        price_five  = PriceService.objects.all()[0].price_five

        auto_price_part = 0

        # Работаем с ценой запчасти 
        
        if self.base_prise <= 100:
            auto_price_part += int(self.base_prise) * (float(part_price_zero)/100)
            auto_price_part = round(auto_price_part / 100) *100

        elif self.base_prise >= 101 and self.base_prise <= 350 :
            auto_price_part += int(self.base_prise) * (float(part_price_one)/100)
            auto_price_part = round(auto_price_part / 100) *100
            
        elif self.base_prise >= 351 and self.base_prise <= 700 :
            auto_price_part += int(self.base_prise) * (float(part_price_two)/100)
            auto_price_part = round(auto_price_part / 100) *100

        elif self.base_prise >= 701 and self.base_prise <= 2000 :
            auto_price_part += int(self.base_prise) * (float(part_price_three)/100)
            auto_price_part = round(auto_price_part / 100) *100

        elif self.base_prise >= 2001 and self.base_prise <= 5001 :
            auto_price_part += int(self.base_prise) * (float(part_price_four)/100)
            auto_price_part = round(auto_price_part / 100) *100

        elif self.base_prise > 5001 :
            auto_price_part += int(self.base_prise) * (float(part_price_five)/100)
            auto_price_part = round(auto_price_part / 100) *100

        else:
            auto_price_part += 1

        if self.autocheck == True:  # Если включена "авто цена" default= True
            # Работаем с ценой ЗЧ + работа ( с округлением)
            if auto_price_part <= 1500:
                price_service_sum = int(auto_price_part) + int(price_one)
                
            elif auto_price_part >= 1501 and auto_price_part <= 3500:
                price_service_sum = int(auto_price_part) + int(price_two)

            elif auto_price_part >= 3501 and auto_price_part <= 7000:
                price_service_sum = int(auto_price_part) + int(price_three)

            elif auto_price_part >= 7001 and auto_price_part <= 10000:
                price_service_sum = int(auto_price_part) + int(price_four)

            elif auto_price_part > 10001:
                price_service_sum = int(auto_price_part) + int(price_five)

            else:
                price_service_sum = 0

        else:
            price_service_sum = self.base_prise
        
        if self.sale == True:
            return ((round(price_service_sum /100)*100) + int(shipping_cost)) - int(self.price_sale) # приводим к виду 200.0
            
        else:
            return (round(price_service_sum /100)*100) + int(shipping_cost) # приводим к виду 200.0
    
    
    def save(self, *args, **kwargs):     
        base_prise = self.base_prise
        self.full_prise = self.sum     
        super(Spare_Part, self).save(*args, **kwargs)

    @property
    def absolute_url(self):
        return reverse('notebook:notebook_home_and_search', kwargs={'name_service': self.name_service})


class Orders(models.Model):
    
    name = models.CharField(" Имя ", max_length=36,  null=True)
    phone_number = PhoneNumberField("Контактный номер", null=True,)
    order_option       = models.CharField(choices=ORDER_OPTION, max_length=1,  null=True,  verbose_name= 'Заказ с выездом?')
    order_day        = models.CharField(choices=ORDER_DAY_OPTION, max_length=1, blank=True, null=True, verbose_name= 'На какой день')
    order_time       = models.CharField(choices=ORDER_TIME_OPTION, max_length=2, blank=True, null=True, verbose_name= 'На какое время')
    location         = models.CharField("Адрес", max_length=200, blank=True, null=True)
    order_problem_name = models.CharField("Название услуги ", max_length=250, blank=True, null=True)
    order_problem_id   = models.CharField("Артикул: услуги", max_length=250, blank=True, null=True)
    read_unread = models.CharField("Статус",choices=READ_UNREAD,max_length=10, default=False, blank=True, null=True)
    final_status_order = models.CharField(choices=MANAGE_ACTION, max_length=2, blank=True, null=True, verbose_name= 'Финальный статус заказа')
    payment  = models.DecimalField("Доход с заявки", blank=True, null=True, max_digits=12, decimal_places=2) 
    created = models.DateTimeField("Заявка создана",auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Заявка обновлена", auto_now_add=False, auto_now=True)




    def __unicode__(self):
        return "ИМЯ %s" "ТЕЛ: %s" "ЗАКАЗ: %s" % (self.name, self.phone_number, self.order_problem_name) 

    class Meta:
        db_table = 'card_order_notebook'
        managed = True
        verbose_name = 'Заказ на ремонт ноутбука'
        verbose_name_plural = 'Заказы на ремонт ноутбука'
    

class OutService(models.Model):
    text_out_service = models.CharField("Условия выезда", max_length=500, blank=True, null=True)
    
    def __unicode__(self):
        return "%s" % (self.text_out_service) 

    class Meta:
        db_table = 'OutService_notebook'
        managed = True
        verbose_name = 'Условия выезда'
        verbose_name_plural = 'Условия выездов'



class DopInfoService(models.Model):
    client_sc = models.TextField("Клиент - сервис (текст)", max_length=1500)
    info_sc = models.TextField("Кто ремонтирует, обязательства, нормативные документы (текст)", max_length=1500)
    info_prise = models.TextField("О ценах и гарантии (текст)", max_length=1500)
    
    def __unicode__(self):
        return "%s"  "%s" "%s"% (self.client_sc, self.info_sc, self.info_prise ) 
 
    class Meta:
        db_table = 'info_service'
        managed = True
        verbose_name = 'Текст на странице товара'
        verbose_name_plural = 'Тексты на странице товара'