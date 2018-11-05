# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *
from accounts.models import *
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
#from .forms import ProfileImageForm
from .forms import CheckoutContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files import File
import os
from django.conf import settings
from django.core.mail import send_mail
from emails.utils import SendingEmail


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    color_check = data.get("color_check")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                    color_check=color_check,
                                                                     is_active=True, defaults={"nmb": nmb})
        if not created:
            print ("not created")
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    #common code for 2 cases
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in  products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        product_dict["color_check"] = item.color_check
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)



def checkout(request):
    user_view = User.objects.filter(id=request.user.id)
    profile   = Profile.objects.filter(id=request.user.id)
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    print (products_in_basket)
    for item in products_in_basket:
        print(item.order)
    
    form = CheckoutContactForm(request.POST, request.FILES)

    if request.method == 'POST':
        print(request.POST)
        if form.is_valid() and  request.user.is_anonymous():
            print ("FORM IS OK")
            request.session["some_variable"] = 1
            print ("some_variable IS OK")
            data = request.POST
            name = data.get("name", "3423453")
            phone = data["phone"]
            address_dostavka = data["address_dostavka"]
            email = data["email"]
            comment_zakaz = data["comment_zakaz"]
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone,
                                                     customer_address=address_dostavka, customer_email = email,
                                                     comments = comment_zakaz )
          
        if request.user.is_authenticated():
            request.session["some_variable"] = 2
            us_name = request.user.username
            name = request.user.first_name
            phone = request.user.profile.tel_number
            address_dostavka = request.user.profile.location
            email = request.user.email
            
            
            data = request.POST
            comment_zakaz = data["comment_zakaz"]
            user = request.user
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone,
                                                     customer_address=address_dostavka, customer_email = email,
                                                     comments = comment_zakaz)

        for name, value in data.items():
            if name.startswith("product_in_basket_"):
                product_in_basket_id = name.split("product_in_basket_")[1]
                product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                print(type(value))
                if request.FILES.get("image"):
                    for file in request.FILES.getlist("image"):
                        instance =  Userimage.objects.create(image=file)

                        instance.save()
                else:
                    messages.error(request, ('Ошибка:Пожалуйста проверьте введенные данные!'))
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
                img_name = instance
                messages.error(request, ('Error:Пожалуйста проверьте введенные данные!'))
                product_in_basket.nmb = value
                product_in_basket.order = order
                product_in_basket.save(force_update=True)
                ProductInOrder.objects.create(product=product_in_basket.product, nmb = product_in_basket.nmb,
                                                price_per_item=product_in_basket.price_per_item, 
                                                color_check = product_in_basket.color_check,
                                                total_price = product_in_basket.total_price,
                                                order=order, us_image=instance)
        #send_mail(u'ТВ-МАСТЕРСКАЯ ОФОРМЛЕН ЗАКАЗ', u'В нашем магазине оформлен новый заказ на сувенирную продукцию!', settings.EMAIL_HOST_USER, ['skret002@yandex.ru'])
        email=SendingEmail()
        email.sending_email(type_id=1, order=order)
        email.sending_email(type_id=2, email=order.customer_email, order=order)

        print(send_mail)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    else:
        #messages.error(request, ('Error:Пожалуйста проверьте введенные данные!'))
        print ("FORM IS BAD")
    return render(request, 'suvenirka_order/checkout.html', locals())
