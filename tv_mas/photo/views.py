# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import *
from photo.models import *
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


# Create your views here.
@csrf_exempt
def photo_home(request):
    args ={}
    head = Header.objects.all()
    info = PhotoInfo.objects.get(pk=1).text
    document_type = DocumentType.objects.all()
    if 'iOS' in request.user_agent.os:
        detect = 'ios'
    else:
        detect = 'other'

    args['detect'] = detect
    args['head'] = head
    args['info'] = info
    args['document_type'] = document_type
    return render(request, 'photo/photo.html', args)


@csrf_exempt
def photo_order(request):
    json_dict = dict()

    try:
        if request.method == 'POST' and request.POST['id_doc']:
            select_id = request.POST['id_doc']
        choice_doc = DocumentType.objects.all()
        for option in choice_doc.filter(id=select_id):
            json_dict["name_document"]  = option.name_document
            json_dict["count"]  = str(option.count_photo)
            json_dict["options_photo"]  = str(option.options_photo)
            json_dict["full_price_photo"]  = str(option.full_price_photo)
            json_dict["edit_price_photo"]  = str(option.edit_price_photo)
            json_dict["image_preview"]  = str(option.image_preview)
    except Exception:
        pass
    if request.method == 'POST' and request.FILES:
        file = request.FILES['image']
        document= DocumentType.objects.get(id=request.POST['select_id'])
        document_name = document.name_document
        name_user = request.POST['first_name']
        phone = request.POST['phone']
        email = request.POST['email']
        task = request.POST['task']
        comment = request.POST['comment']
        order = OrderPhoto.objects.create(status='1', name_document=document_name, name_user=name_user, email=email, phone_number=phone,
                                 task=task, you_file=file, comment=comment)
        order.save()
        send_mail(u'ТВ-МАСТЕРСКАЯ - НОВОЕ ФОТО НА ДОКИ', u'Новый заказ - "фото на документы", срочно посетите админку.', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
        number_order = str(order.id)
        json_dict["number_order"]  = number_order
        choice_doc = DocumentType.objects.all()
        for option in choice_doc.filter(id=request.POST['select_id']):
            json_dict["name_document"]  = option.name_document
            json_dict["full_price_photo"]  = str(option.full_price_photo)
            json_dict["edit_price_photo"]  = str(option.edit_price_photo)
        respondent = Respondent.objects.all()
        for item in respondent:
            json_dict["name_respondent"] = item.name
            json_dict["phone_respondent"] = item.phone
            json_dict["namber_bank_respondent"] = item.namber_bank
            
    return JsonResponse(json_dict)