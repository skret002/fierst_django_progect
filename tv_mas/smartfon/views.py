# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from smartfon.models import *
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django_user_agents.utils import get_user_agent
from emails.utils import SendingEmail
from django.db.models import Q
from django.http import JsonResponse
#from gadget_parts_pars import *
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
from .forms import Orders
from django.core.paginator import Paginator
from django.conf import settings
import re

# Create your views here.
def smartfon_home_and_search(request):
    args ={}
    smarfon_data = []
    json_dict = dict()
    if request.method == 'GET'  and request.GET.get("input_model"):
        data = request.GET
        search_model = data.get("input_model")
        args['search_model'] = search_model
        if search_model:
            choise_models_bd = SmartfonModels.objects.all().filter(model__icontains=search_model) 
            args['choise_models_bd'] = choise_models_bd
            for i in choise_models_bd:
                smarfon_data.append({
                    'id': i.id,
                    'name': i.model,
                    'brend' : i.brend_key.brend,
                })
                cache.set('smarfon_data',(smarfon_data))


            
            count_jast_model = choise_models_bd.all().count()
            args['count_jast_model'] = count_jast_model
            count_val = args.get('count_jast_model')
            args['count_val'] = count_val
            cache.set('my_key',(args))
            cache.add('my_key',(args))

        # популярные услуги 
    popular_services = Spare_Part.objects.all().filter(popular_service=True) 
    args['popular_services'] = popular_services
        # товары по акции
    sale = Spare_Part.objects.all().filter(sale=True) 
    args['sale'] = sale
  
    return render(request, 'smartfon/remont_smartfonov.html',args)
    

def smarfon_search_result(request):
    json_dict = dict()
    args = cache.get('my_key')
    smarfon_data= cache.get('smarfon_data')
    smarfon_data_id = []
    smarfon_data_name = []
    smarfon_data_brend= []
    for i in smarfon_data:
        smarfon_data_id.append({'id' : i['id']})
        smarfon_data_name.append({'name': i['name']})
        smarfon_data_brend.append({'brend': i['brend']})
    if request.method == 'GET':
        try:
            json_dict["count_val"]= args['count_val']
        except TypeError:
            json_dict["count_val"]= 'error_count_val'
    


    json_dict["smarfon_data"]= smarfon_data
    json_dict["smarfon_data_id"]= smarfon_data_id
    json_dict["smarfon_data_name"]= smarfon_data_name
    json_dict["smarfon_data_brend"]= smarfon_data_brend
    return JsonResponse(json_dict)


@csrf_exempt
def SmartfonService(request, model_name, model_id, brend=None, page_number=1):
    args    ={}
    services_and_price = Spare_Part.objects.all().filter(smartfonmodels=model_id, autocheck=True)
    sale    = Spare_Part.objects.all().filter(sale=True) 
    action_problem      = ActionProblem.objects.all()   # in chaine
    quality_part = QualityPart.objects.all()   # in chaine
    choices_available = ChoicesAvailable.objects.all()   # in chaine
    product_s = Spare_Part.objects.all().filter(smartfonmodels=model_id)
    product = Paginator(product_s,15)

    if request.method == 'POST' and request.POST.get("choices_available"):
        print(request.POST)
        if request.POST.get('problem'):
            problem = request.POST.get('problem')
            choice_problem = ActionProblem.objects.filter(id=problem) # определяем выбранную проблему
            print(problem)
            print(choice_problem)
            args['choice_problem'] = choice_problem   # после фильтрации ставим выбранное в TITLE
        else:
            problem = None

        if request.POST.get('quality_part') and int(request.POST.get('quality_part')) !=5:
            quality_part = request.POST.get('quality_part')
            choice_quality_part = QualityPart.objects.filter(id=quality_part)
            args['choice_quality_part'] = choice_quality_part   # после фильтрации ставим выбранное в TITLE
        else:
            quality_part = None

        if request.POST.get('choices_available') and (request.POST.get('choices_available')!= '4') :
            choices_available = request.POST.get('choices_available')
        else:
            choices_available = None
        
        sort = {}
        pre_sort={'action_problem':problem, 'quality_part':quality_part, 'available_part':choices_available}
        
        for key in pre_sort:
            if pre_sort[key] is not None:
                sort.update({key:pre_sort[key] })
        product_sort = Spare_Part.objects.filter(smartfonmodels=model_id, **sort )
        product = Paginator(product_sort,15)
        quality_part = QualityPart.objects.all()   # in chaine
        choices_available = ChoicesAvailable.objects.all()   # in chaine

    form_order = Orders(request.POST)   
    args['form_order'] = form_order
    if request.method == 'POST' and request.POST.get("phone_number"):
        print("ЕСТЬ ЗАПРОС")
        if form_order.is_valid():
            data = request.POST
            print(data["phone_number"])
            data  = form_order.cleaned_data
            form_order.save()
            success_url = request.META.get('HTTP_REFERER','/') +"#success_order" #
            send_mail(u'ТВ-МАСТЕРСКАЯ ВОПРОС ПО РЕМОНТУ ТВ', u'Оформлен новый заказ на ремонт смартфона & планшета.', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
            return HttpResponseRedirect(success_url) # 
            
        else:
            error_url = request.META.get('HTTP_REFERER','/') +"#order_error"
            return HttpResponseRedirect(error_url) # 

    outservice = OutService.objects.all() 

    #page_paginator_link
    current = []
    host = request.META['HTTP_HOST']
    url_now = request.get_full_path()
    url_index = re.sub(r'\(/0-9]+\)', '/', url_now)[-2]
    prev_url = int(url_index) -1
    next_url = int(url_index) +1

    for page in product.page_range:
        
        current.append({'url' : 'http://'+str(host)+'/'+'remont_smartfona'+'/'+str(brend)+'/'+ str(model_name)+'/'+str(model_id)+'/'+str(page)+'/',
                        'page_num': str(page),
                        'prev_url': 'http://'+str(host)+'/'+'remont_smartfona'+'/'+str(brend)+'/'+ str(model_name)+'/'+str(model_id)+'/'+str(prev_url)+'/',
                        'next_url': 'http://'+str(host)+'/'+'remont_smartfona'+'/'+str(brend)+'/'+ str(model_name)+'/'+str(model_id)+'/'+str(next_url)+'/',})
    page_prev = current[-1]['prev_url']
    page_next = current[-1]['next_url']

    args['max_page'] = str(product.page_range[-1])
    args['url_index'] = str(url_index)
    args['page_prev'] = page_prev
    args['page_next'] = page_next
    args['current'] = current
    args['outservice'] = outservice
    args['quality_part'] = quality_part
    args['choices_available'] = choices_available
    args['action_problem'] = action_problem
    #args['filters'] = filters
    args['product'] = product.page(page_number)
    args['model_name'] = model_name
    args['model_id'] = model_id
    args['brend'] = brend
    args['sale'] = sale
    args['services_and_price'] = services_and_price
    return render(request, 'smartfon/service_smartfon.html',args)

def PartsCart(request, model_name, model_id, problem, name_part = None):
    args ={}
    product = Spare_Part.objects.filter(smartfonmodels=model_id, name_service=problem)
    dopinfoservice = DopInfoService.objects.all()
                    # Форма заказа повторяется из предыдущей функции включая js
    form_order = Orders(request.POST)   
    args['form_order'] = form_order
    if request.method == 'POST' and request.POST.get("phone_number"):
        if form_order.is_valid():
            data = request.POST
            print(data)
            data  = form_order.cleaned_data
            form_order.save()
            success_url = request.META.get('HTTP_REFERER','/') +"#success_order" #
            send_mail(u'ТВ-МАСТЕРСКАЯ ВОПРОС ПО РЕМОНТУ ТВ', u'Оформлен новый заказ на ремонт смартфона & планшета.', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
            return HttpResponseRedirect(success_url) # 
            
        else:
            error_url = request.META.get('HTTP_REFERER','/') +"#order_error"
            return HttpResponseRedirect(error_url) # 

    
    args['problem'] = problem
    args['model_name'] = model_name
    args['dopinfoservice'] = dopinfoservice
    args['product'] = product
    return render(request, 'smartfon/parts_cart.html',args)

def SalePartsCart(request, name_part):
    args ={}
    print(name_part)
    product = Spare_Part.objects.filter(name_service=name_part)
    dopinfoservice = DopInfoService.objects.all()
                    # Форма заказа повторяется из предыдущей функции включая js
    form_order = Orders(request.POST)   
    args['form_order'] = form_order
    if request.method == 'POST' and request.POST.get("phone_number"):
        if form_order.is_valid():
            data = request.POST
            print(data)
            data  = form_order.cleaned_data
            form_order.save()
            success_url = request.META.get('HTTP_REFERER','/') +"#success_order" #
            send_mail(u'ТВ-МАСТЕРСКАЯ ВОПРОС ПО РЕМОНТУ ТВ', u'Оформлен новый заказ на ремонт смартфона & планшета.', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
            return HttpResponseRedirect(success_url) # 
            
        else:
            error_url = request.META.get('HTTP_REFERER','/') +"#order_error"
            return HttpResponseRedirect(error_url) # 

    args['name_part'] = name_part
    args['dopinfoservice'] = dopinfoservice
    args['product'] = product
    return render(request, 'smartfon/sale_part_cart.html',args)