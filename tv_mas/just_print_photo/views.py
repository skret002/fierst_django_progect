# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import *
from just_print_photo.models import *
from django.template import loader, RequestContext
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.core.mail import send_mail
from django_user_agents.utils import get_user_agent
from django.core.paginator import Paginator
from emails.utils import SendingEmail
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
from user_agents import parse
import re

# Create your views here.
@csrf_exempt
def print_photo_home(request):
    args ={}
    head = PrintPhotoHeader.objects.all()
    try:
        info = PrintPhotoInfo.objects.get(pk=1).text
    except Exception:
        info = ''

    price_photo = PhotoProdukt.objects.all()
#    if 'iOS' in request.user_agent.os:
#        detect = 'ios'
#    else:
#        detect = 'other'
#
#    args['detect'] = detect
    args['head'] = head
    args['info'] = info
    args['price_photo'] = price_photo
    return render(request, 'just_print_photo/photo.html', args)


@csrf_exempt
def print_photo_order(request):
    json_dict = dict()
    if request.method == 'POST' and request.FILES:
        print(request.POST)
        number = NumberOrder.objects.all() 
        try:
            number_order_new = int(number.last().number_order) + 1
        except AttributeError:
            number_order_new = 100
        count_line = request.POST['count_line']
        try:
            task = request.POST['task']
        except Exception:
            task = '0'
            
        number_order, created  = NumberOrder.objects.get_or_create(number_order = str(number_order_new))
        user, created  = Customer.objects.get_or_create(name_user = request.POST['first_name'], 
                                                        phone_number = request.POST['phone'],
                                                        email = request.POST['email'], )
        order_photo, created = Order.objects.get_or_create(number_orders = number_order,
                                                            status = '1',
                                                            user = user,
                                                            comment = request.POST['comment'],
                                                            count_price = request.POST['fullprice'],
                                                            task_call=task
                                                            )
         
        if count_line:
            pass
        else:
            count_line = 0

        for x in range(int(count_line)+1):
            product = PhotoProdukt.objects.get(pk = request.POST['type_photo_'+str(x)])
            if request.FILES.get("file-"+str(x)):
                for file in request.FILES.getlist("file-"+str(x)):
  
                    option, created  = OptionPhotoField.objects.get_or_create(
                                                                        files = file,
                                                                        count_photo = request.POST['count_copy_'+str(x)],
                                                                        order = order_photo,
                                                                        photo_product = product,
                                                                        with_margin = request.POST['field_select_'+str(x)],
                                                                        time_take = request.POST['time_'+str(x)],)
            instance =  FilePhoto.objects.create(options=option)
            instance.save()  
        send_mail(u'ТВ-МАСТЕРСКАЯ - НОВЫЕ ФОТОГРАФИИ', u'Новый заказ - "фотографии на печать ", срочно посетите админку.', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
    respondent = RespondentForPhoto.objects.all()
    print(respondent)
    for item in respondent:
        json_dict["name_respondent"] = item.name
        json_dict["phone_respondent"] = item.phone
        json_dict["namber_bank_respondent"] = item.namber_bank                                              
    json_dict['number_order_new'] = number_order_new
    return JsonResponse(json_dict)