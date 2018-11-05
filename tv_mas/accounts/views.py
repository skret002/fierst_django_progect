# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from forms import UserForm, ProfileForm,RegistrationForm
from django.db import transaction
from django.contrib import messages
from suvenirka_order.models import *
from suvenirka_product.models import *
from accounts.models import *
from suvenirka_product.forms import QuestionProdukt
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

#@login_required
#def home(request):
#    return render(request, 'update_profile')

def login_all(request):
    if request.POST:
        print('POST')
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("auth is ok!")
            print(request.META.get('HTTP_REFERER'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            args['login_error']="Пользователь не найден"
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return render(request, 'accounts/log_all.html', locals())



def signup(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_profile')
    else:
        form = RegistrationForm()

        args = {'form': form}
    return render(request, 'accounts/signup.html', {'form': form})



@login_required
def view_profile(request):
    form = QuestionProdukt(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print ("FORMA VOPROSA PROSHLA")
        data  = form.cleaned_data
        data = request.POST
        you_name = request.user.username
        you_phone = request.user.profile.tel_number
        you_question = data["you_question"]
        print (data)
        paf= request.path
        paf_url=paf
        print (paf_url)
        instance =  IssuesProdukt.objects.create(issues_url=paf_url,you_name=you_name,you_phone=you_phone,you_question=you_question)
        instance.save()
        messages.success(request, ('Ваш вопрос получен. Наш менеджер свяжется с Вами в близжайшее время!'))
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    user_view = User.objects.filter(id=request.user.id)
    profile   = Profile.objects.filter(id=request.user.id)
    orders = ProductInOrder.objects.filter(order__user=request.user.id)


    return render(request, 'accounts/profile_view.html', locals())



@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        print('POST')
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Ваши данные успешно обновлены'))
            print('form too is valid')
            return redirect('update_profile')
        else:
            messages.error(request, ('Error:Пожалуйста проверьте введенные данные!'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
