# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import *
from repair_tv.models import *
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
from .forms import QuestionTV, OrderingServices
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from itertools import chain

# Create your views here.


def repair_tv_home(request):
    tv_brend = BrendTv.objects.filter(is_active=True)[ :12]
    text_tv_home = TextTvHome.objects.all()
    ##  height section in css
    css_h = BrendTv.objects.all()[ :12]
    h = len(css_h.values('brend'))
    h_css = int(round(h / 3.0) * 267) # in tamplate remont_televizorov.html
    
    return render(request, 'repair_tv/remont_televizorov.html', locals())


@csrf_exempt
def brend_detail(request, brend):
    args = {}
    tv_brend = BrendTv.objects.filter(brend=brend)
    tv_models = Tv_Models.objects.filter(is_brend__brend=brend)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

#####################  просто DJANGO FORM    
    form_q = QuestionTV(request.POST, request.FILES)
    args['form_q'] = form_q

    if request.method == 'POST' and request.FILES :
        session_key = request.session.session_key
        print("POST and FILE READY")
        if form_q.is_valid():
            data  = form_q.cleaned_data
            data = request.POST
            print(data)
            you_name = data["you_name"]
            print (you_name)
            phone = data["phone"]
            you_email = data["you_email"]
            tv_brend = data["tv_brend"]
            tv_model = data["tv_model"]
            you_question = data["you_question"]
            you_file = request.FILES['you_file']
            form_q.save()
            send_mail(u'ТВ-МАСТЕРСКАЯ ВОПРОС ПО РЕМОНТУ ТВ', u'Оформлен новый вопрос по темонту ТВ, клиент ожидает ответа.', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
            return HttpResponseRedirect(request.META['HTTP_REFERER'])


    if request.method == 'POST':
        session_key = request.session.session_key
        print("POST READY")
        if form_q.is_valid():
            data  = form_q.cleaned_data
            data = request.POST
            print(data)
            you_name = data["you_name"]
            print (you_name)
            phone = data["phone"]
            you_email = data["you_email"]
            tv_brend = data["tv_brend"]
            tv_model = data["tv_model"]
            you_question = data["you_question"]
            form_q.save()
            
            send_mail(u'ТВ-МАСТЕРСКАЯ ВОПРОС ПО РЕМОНТУ ТВ', u'Оформлен новый вопрос по темонту ТВ, клиент ожидает ответа.', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

    if brend:
        brend = BrendTv.objects.get(brend=brend)
        args['brend'] = brend
        print (brend)
    
    quare=request.GET.get('q')
    args['quare'] = quare
    #print(quare)
    if quare:
        service_list= Tv_Models.objects.all().filter(number_tv_model__icontains=quare) 
        args['service_list'] = service_list
        if service_list:
            m = 1
        
        else:
            m = 2
        
        print(m)
        args['m'] = m
        print(service_list)

    data = request.GET
    choise_model = data.get("model_number")
    print("Выбрана модель")
    print(choise_model)
    servise_to_model = Tv_Repair.objects.filter(number_tv_model__pk=choise_model)
    models = Tv_Models.objects.filter(id=choise_model)
    args['models'] = models
    service_all_model = Tv_Repair.objects.filter(kgn='2')
    args['service_all_model'] = service_all_model
    base_service = Tv_Repair.objects.filter(id=15)[0].service
    args['base_service'] = base_service
    if servise_to_model: 
        servise_under_f = list(chain(servise_to_model, service_all_model)) 
    else:
        servise_under_f = list(chain(models, service_all_model)) 
    
    args['tv_brend'] = tv_brend
    args['tv_models'] = tv_models
    args['quare'] = quare
    args['choise_model'] = choise_model
    args['servise_to_model'] = servise_to_model
    args['servise_under_f'] = servise_under_f
    print("**************")
    print(servise_under_f)
    print("**************")
    return render(request, 'repair_tv/brend_detail.html', args)


@csrf_exempt
def RepairService(request, brend, service, model):
    args = {}
    if request.method == 'POST' and request.POST.get("choiceservice"):
        print("POST YES")
        data = request.POST
        choiceservice = data["choiceservice"]
        #print(choiceservice)
        tv_repair = Tv_Repair.objects.filter(id=choiceservice)
        model     = Tv_Models.objects.filter(number_tv_model=model)
        args['tv_repair'] = tv_repair
        args['model'] = model
    else:     
        print ("choiceservice NET")
        #return HttpResponseRedirect(request.META['HTTP_REFERER'])

    form = OrderingServices(request.POST)
    args['form'] = form
    if request.method == 'POST':
        if "name" in request.POST:
            print(request.POST, "POST")
            if form.is_valid():
                data  = form.cleaned_data
                order = form.save(commit=False)
                order.brend_tv = brend
                order.model_tv = model
                order.crash = service
                print(order)
                data = request.POST  
                name = data["name"]
                phone = data["phone"]
                time  = data["time"]
                additional_message = data["additional_message"]
                form.save()
                send_mail(u'ТВ-МАСТЕРСКАЯ ВОПРОС ПО РЕМОНТУ ТВ', u'Оформлен новый заказ на ремонт ТВ, клиент ожидает ответа.', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
                
        else:
            print("NOT NAME")



    return render(request, 'repair_tv/repair_service.html', args)