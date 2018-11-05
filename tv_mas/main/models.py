# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Title_pape(models.Model):
    title_on_pape       = models.CharField(max_length = 80,  blank = True, verbose_name ='TITLE страницы')
    description_on_pape = models.CharField(max_length = 200, blank = True, verbose_name ='Описание страницы')
    keywords_on_pape    = models.CharField(max_length = 150, blank = True, verbose_name ='Ключевые слова страницы')
    yandex_key          = models.CharField(max_length = 250, blank = True, verbose_name ='ключ яндекса')
    google_key          = models.CharField(max_length = 250, blank = True, verbose_name ='ключ google ')
    snipet              = models.TextField(max_length = 500, blank = True, verbose_name ='Можно поставить свой снипет cod')
    created             = models.DateTimeField (auto_now_add=True, auto_now=False)
    updates             = models.DateTimeField (auto_now_add=False, auto_now=True)
    class Meta:
        verbose_name        = "TITLE + META"
        verbose_name_plural = "TITLE + META"
    
    def __unicode__(self):
        return "META описания для %s" %(self.title_on_pape)



class Top_item(models.Model):
    telephone = models.CharField(max_length = 24, blank = True, verbose_name ='Телефоны в ТОПЕ')
    address = models.CharField(max_length = 60, blank = True, verbose_name ='Адрес в ТОПЕ')
    text1 = models.CharField(max_length = 200, blank = True, verbose_name ='Текст в TOP :1')
    text2 = models.CharField(max_length = 200, blank = True, verbose_name ='Текст в TOP :2')
    text3 = models.CharField(max_length = 200, blank = True, verbose_name ='Текст в TOP :3')
    text4 = models.CharField(max_length = 200, blank = True, verbose_name ='Текст в TOP :4')

    class Meta:
        verbose_name = "Текс для верхний части "
        verbose_name_plural = "Текс для верхний части"

    def  __unicode__(self):
        return "item - %s %s %s %s" % (self.text1, self.text2, self.text3, self.text4)      



class Home_and_base(models.Model):
    short_name  = models.CharField(max_length = 30, verbose_name ='Короткое название')
    stati_title = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи')
    stati_text  = models.TextField(blank = True, verbose_name ='Тело Статьи')

    short_name2  = models.CharField(max_length = 30, verbose_name ='Короткое название :2')
    stati_title2 = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи :2')
    stati_text2  = models.TextField(blank = True, verbose_name ='Тело Статьи :2')

    short_name3  = models.CharField(max_length = 30, verbose_name ='Короткое название :3')
    stati_title3 = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи :3')
    stati_text3  = models.TextField(blank = True, verbose_name ='Тело Статьи :3')

    short_name4  = models.CharField(max_length = 30, verbose_name ='Короткое название4')
    stati_title4 = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи4')
    stati_text4  = models.TextField(blank = True, verbose_name ='Тело Статьи4')

    short_name5  = models.CharField(max_length = 30, verbose_name ='Короткое название :5')
    stati_title5 = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи :5')
    stati_text5  = models.TextField(blank = True, verbose_name ='Тело Статьи :5')

    short_name6  = models.CharField(max_length = 30, verbose_name ='Короткое название6')
    stati_title6 = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи6')
    stati_text6  = models.TextField(blank = True, verbose_name ='Тело Статьи6')

    short_name7  = models.CharField(max_length = 30, verbose_name ='Короткое название :7')
    stati_title7 = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи :7')
    stati_text7  = models.TextField(blank = True, verbose_name ='Тело Статьи :7')

    short_name8  = models.CharField(max_length = 30, verbose_name ='Короткое название :8')
    stati_title8 = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи :8')
    stati_text8  = models.TextField(blank = True, verbose_name ='Тело Статьи :8')

    short_name9  = models.CharField(max_length = 30, verbose_name ='Короткое название :9')
    stati_title9 = models.CharField(max_length = 200, blank = True, verbose_name ='Заголовок статьи :9')
    stati_text9  = models.TextField(blank = True, verbose_name ='Тело Статьи :9')

    class Meta:
        verbose_name = "СТАТЬЯ"
        verbose_name_plural = "СТАТЬИ"

    def  __unicode__(self):
       return " %s" %(self.short_name)      



class Footer_item(models.Model):
    text1 = models.CharField(max_length = 200, blank = True, verbose_name ='Текст в footer :1')
    text2 = models.CharField(max_length = 200, blank = True, verbose_name ='Текст в footer :2')
    text3 = models.CharField(max_length = 200, blank = True, verbose_name ='Текст в footer :3')
    text4 = models.CharField(max_length = 200, blank = True, verbose_name ='Текст в footer :4')

    class Meta:
        verbose_name = "Текс для footer "
        verbose_name_plural = "Текс для footer"

    def  __unicode__(self):
        return "item - %s %s %s %s" % (self.text1, self.text2, self.text3, self.text4) 

