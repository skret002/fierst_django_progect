# -*- coding: utf-8 -*-
from suvenirka_product.models import *
from accounts.models import *
from slider_up.models import Slider_up
from slider_up.models import Slider_image, Slider_image_tablet, Slider_image_mobile
from slider_up.models import Description_suvenirka
from .forms import PriceFilter
from .forms import QuestionProdukt
from django.template import loader, RequestContext
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.core.mail import send_mail
from django_user_agents.utils import get_user_agent
from django.core.paginator import Paginator
from emails.utils import SendingEmail

def product(request, list_produkts_id):
    product = Product.objects.get(id=list_produkts_id)
    list_produkt = Product.objects.filter(id=list_produkts_id)
    list_categori = ProductCategory.objects.all()


    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()

    print(request.session.session_key)
    form = QuestionProdukt(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid() and request.user.is_anonymous():
            print ("FORMA VOPROSA PROSHLA")
            data  = form.cleaned_data
            data = request.POST

            you_name = data["you_name"]
            you_phone = data["you_phone"]
            you_question = data["you_question"]
            print (data)
            paf= request.path
            paf_url=paf
            print (paf_url)
            instance =  IssuesProdukt.objects.create(issues_url=paf_url,you_name=you_name,you_phone=you_phone,you_question=you_question)
            instance.save()
            messages.success(request, ('Ваш вопрос получен. Наш менеджер свяжется с Вами в близжайшее время!'))
            send_mail(u'ТВ-МАСТЕРСКАЯ ОФОРМЛЕН ЗАКАЗ', u'В нашем магазине задан вопрос по сувенирной продукции', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
        if request.user.is_authenticated():
            data  = form.cleaned_data
            data = request.POST
            you_name = request.user.username
            print(you_name)
            print('zashli authenticated')
            you_phone =  request.user.profile.tel_number
            you_question = data["you_question"]
            paf= request.path
            paf_url=paf
            print (paf_url)
            instance =  IssuesProdukt.objects.create(issues_url=paf_url,you_name=you_name,you_phone=you_phone,you_question=you_question)
            instance.save()
            messages.success(request, ('Ваш вопрос получен. Наш менеджер свяжется с Вами в близжайшее время!'))
            send_mail(u'ТВ-МАСТЕРСКАЯ ОФОРМЛЕН ЗАКАЗ', u'В нашем магазине задан вопрос по сувенирной продукции', settings.EMAIL_HOST_USER, ['79219032885@ya.ru'])
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        #new_form = form.save()

    return render(request, 'suvenirka_product/product.html', locals())

def suvenirka_home(request):
    user_agent = get_user_agent(request)
    print(user_agent)
    slider_and_text1 = Slider_up.objects.all()[0:1]
    slider_and_text2 = Slider_up.objects.all()[1:2]
    slider_and_text3 = Slider_up.objects.all()[2:3]
    slider_and_text4 = Slider_up.objects.all()[3:4]
    meta_title = Description_suvenirka.objects.all()[0:1]
    if user_agent.is_pc:
        slider_and_image1 = Slider_image.objects.all()[0:1]
        slider_and_image2 = Slider_image.objects.all()[0:2]
        slider_and_image3 = Slider_image.objects.all()[0:3]
        slider_and_image4 = Slider_image.objects.all()[0:4]

    elif user_agent.is_tablet:
        slider_and_image1 = Slider_image_tablet.objects.all()[0:1]
        slider_and_image2 = Slider_image_tablet.objects.all()[0:2]
        slider_and_image3 = Slider_image_tablet.objects.all()[0:3]
        slider_and_image4 = Slider_image_tablet.objects.all()[0:4]
    
    if user_agent.is_mobile:
        slider_and_image1 = Slider_image_mobile.objects.all()[0:1]
        slider_and_image2 = Slider_image_mobile.objects.all()[0:2]
        slider_and_image3 = Slider_image_mobile.objects.all()[0:3]
        slider_and_image4 = Slider_image_mobile.objects.all()[0:4]
    return render(request, 'suvenirka_product/suvenirka.html', locals())


def all_suvenirka_product(request, produkt_page=1):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, is_active=True, is_main=True, product__is_active=True)
    current_products = Paginator(products_images, 8)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    return render_to_response('suvenirka_product/all_produkt.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":current_products.page(produkt_page), "products_color":products_color})


def krugka_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=1, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 1)

    return render_to_response('suvenirka_product/krugka_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def chehlu_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=2, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 2)

    return render_to_response('suvenirka_product/chehlu_produkt.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def futbolki_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=3, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 3)

    return render_to_response('suvenirka_product/futbolki_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})


def tarelki_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=4, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 4)

    return render_to_response('suvenirka_product/tarelki_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def watch_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=5, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 5)

    return render_to_response('suvenirka_product/watch_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def pazlu_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=6, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 6)

    return render_to_response('suvenirka_product/pazlu_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def kalendari_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=7, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 7)

    return render_to_response('suvenirka_product/kalendari_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def podushki_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=8, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 8)

    return render_to_response('suvenirka_product/podushki_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def magnitu_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=9, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 9)
    return render_to_response('suvenirka_product/magnitu_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})



def poster_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=10, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 10)

    return render_to_response('suvenirka_product/poster_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})


def bs_fl_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=11, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 11)

    return render_to_response('suvenirka_product/bs_fl.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def nabor_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=12, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 12)

    return render_to_response('suvenirka_product/nabor_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def meshki_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=13, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 13)

    return render_to_response('suvenirka_product/meshki_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def drugie_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=14, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 14)

    return render_to_response('suvenirka_product/drugie_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def pano_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=15, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 15)

    return render_to_response('suvenirka_product/pano_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def holst_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=16, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 16)

    return render_to_response('suvenirka_product/holst_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def sumki_i_obuv_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=17, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 17)

    return render_to_response('suvenirka_product/sumki_i_obuv_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def kolaj_na_holste_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=18, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 18)

    return render_to_response('suvenirka_product/kolaj_na_holste_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def shirokofor_pechat(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=19, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 19)

    return render_to_response('suvenirka_product/shirokofor_pechat.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def r_kartin(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=20, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 20)

    return render_to_response('suvenirka_product/r_kartin.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def domovue_znaki(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=21, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 21)

    return render_to_response('suvenirka_product/domovue_znaki.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def info_znaki(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=22, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 22)

    return render_to_response('suvenirka_product/info_znaki.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def tablichki_plastik(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=23, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 23)

    return render_to_response('suvenirka_product/tablichki_plastik.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def tablichki_fsk(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=24, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 24)

    return render_to_response('suvenirka_product/tablichki_fsk.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def teh_tablichki(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=25, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 25)

    return render_to_response('suvenirka_product/teh_tablichki.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})


def neft_gaz(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=26, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 26)

    return render_to_response('suvenirka_product/neft_gaz.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def jd_dorogi(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=27, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 27)

    return render_to_response('suvenirka_product/jd_dorogi.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def portret_pamyatnik(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=28, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 28)

    return render_to_response('suvenirka_product/portret_pamyatnik.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def ritualnue_tablichki(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=29, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 29)

    return render_to_response('suvenirka_product/ritualnue_tablichki.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def kompozicii(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=30, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 30)

    return render_to_response('suvenirka_product/kompozicii.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def graf_kompozicii(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=31, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 31)

    return render_to_response('suvenirka_product/graf_kompozicii.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def arki_kompozicii(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=32, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 32)

    return render_to_response('suvenirka_product/arki_kompozicii.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def keramika_izo(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=33, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 33)

    return render_to_response('suvenirka_product/keramika_izo.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def gold_arnamentu(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=34, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 34)

    return render_to_response('suvenirka_product/gold_arnamentu.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def metal_photo(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=35, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 35)

    return render_to_response('suvenirka_product/metal_photo.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def grafiti(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=36, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 36)

    return render_to_response('suvenirka_product/grafiti.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def portretu_pod_jivopis(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=37, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 37)

    return render_to_response('suvenirka_product/portretu_pod_jivopis.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def kalendari_product(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=7, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 7)

    return render_to_response('suvenirka_product/kalendari_product.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})

def foto_na_stekle(request):
    form = PriceFilter(request.GET)
    if form.is_valid():
        min_price = request.GET.get('min_price',default='1') 
        max_price =  request.GET.get('max_price', default="999999999")

        print (min_price)
        print (max_price)
    products_images = ProductImage.objects.filter(product__price__gte=min_price or 1, product__price__lte=max_price or 999999, product__category__id=38, is_active=True, is_main=True, product__is_active=True)
    list_produkt = Product.objects.all()
    list_categori = ProductCategory.objects.all()
    products_color = ColorField.objects.all()
    description_kategori =  Description_Category.objects.filter(page__id = 38)

    return render_to_response('suvenirka_product/foto_na_stekle.html', {"form" : form,  "list_categori":list_categori , "list_produkt":list_produkt, "products_images":products_images, "products_color":products_color, "description_kategori":description_kategori})