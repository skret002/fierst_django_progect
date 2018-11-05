# -*- coding: utf-8 -*-
from celery.task import task
from celery.schedules import crontab
from tv_mas.celery_app import app
from smartfon.models import *
from .gadget_parts_pars import *
import time
import re

__autor__ = 'mevlutov'


@app.task
def main():
    rename_at_apple = [('Home'),('bluetooth'),('3G'),('610A3B'),]
    mod_del  = [('Home'),('bluetooth'),('3G'),('610A3B'),('Mate'),('Hоme'),('GPS'),('Wi-Fi'),
                ('wifi'),('NFC'),('U2'),('1608А2'),('PM8019'),('Space'),('HQ'),]
    clear_data = []    # готовые данные для записи в БД
    pre_clear = []     #  мусорка
    all_page = []     # адреса всех стр.
    all_cart_url = list()  # выбераем все ссылки на карточки товаров
    url_part = []

    count_page = int(get_pages(get_html_gadget(BASE_URL)))
    for page in range(1, count_page +1):    # сколько страниц проходим?
        #print(page)
        all_page.append(BASE_URL + str(page) +"/")

    for page_url in all_page:       # выбераем все ссылки на карточки товаров
        all_cart_url += (get_part_url(get_html_gadget(page_url)))
    c = 0  # начало счета страница
    try:
        for item in all_cart_url:
            c += 1
            if ( c%18) == 0:
                sleep(randint(1,3))      
            try:
                data = info_part(get_html_gadget(base_host+item))
                pre_clear.append(data)
            except ConnectionError:
                pass
    except TypeError:
        pass

    for item in pre_clear:
        try:
            des =str(item[3]['product__description']) # описание услуги
            deskript  = str(des.replace('нашем интернет-магазине','нашем сервисе').replace('приобрести','заменить'))
        except(IndexError, KeyError, TypeError):
            deskript = str("еще не успели написать :)")
        try:
            price = item[1]['price']
        except(KeyError, IndexError):
            price = 0
        try:
            img = item[4]['image_local']
        except(IndexError, KeyError, TypeError):
            img = str(img_sm_device + "font/" + 'no_im.png')
        try:
            av_p = int(item[2]['count'])
        except(IndexError, KeyError, TypeError): 
            av_p = 0
        try:
            if any(x in (item[0]['name_part']) for x in word_delete):
                print("пропускаю word_delete")
                pass
            else:
                t_clear = str(item[0]['name_part'])

                cl_t = t_clear
                if any(x in cl_t for x in word_original):
                    quality_part = 1
                else:
                    quality_part = 2
                if any(x in cl_t for x in word_repair_place):
                        repair_place = 2
                else:
                    repair_place = 1

                try:
                    if av_p > 1:
                        available_part = 1
                    elif av_p == 1:
                        available_part = 2
                    else:
                        available_part = 3
                except KeyError:
                    available_part = 3
                action_problem = problem_name_service(cl_t + t_clear)
                act_problem = action_problem
                name = ''
                count_r_el = int(len(word_replace_in_name))
                name_do_rep = str(cl_t)
                name_too = ''
                if any(x in name_do_rep for x in word_replace_in_name):
                    name = name_do_rep
                    print('name',name)
                    while any(x in name for x in word_replace_in_name):
                        for r in word_replace_in_name: 
                            name = name.replace(r, 'ЗАМЕНЕНО')
                else:
                    while any(x in name for x in word_replace_in_name):
                        for r in word_replace_in_name: 
                            name = cl_t.replace(r, 'ЗАМЕНЕНО')
                            print('name',name)

                        #s2 = re.sub(r'\([A-Za-z0-9]+\)', '', name)  
                if name == '':
                    r = re.sub(r'([а-яА-я]+)','', cl_t)
                    rs = re.findall(r'([A-Za-z0-9]+)', r) 
                    print('ИМЯ БЫЛО ПУСТОЕ', rs) 
                else:
                    r = re.sub(r'([а-яА-я]+)','', name)
                    print("NORUS", r)
                    rs = re.findall(r'([A-Za-z0-9]+)', r)
                    print('rs', rs)
                t = ' '.join(rs)  
                print('t', t)
                model = ''
                if any(ap in cl_t for ap in apple_detect):
                    mp = t.split()[0:3]
                    model =  ' '.join(mp)
                    print("АППЛ")
                    brend = 'Apple'  
                else:
                    print("Не АППЛ")
                    mp = t.split()[0:]
                    model =  ' '.join(mp)
                    brend = t.split()[0]

                if brend == 'iPad' or brend == 'iPhone':
                    brend = 'Apple'
                elif  brend == 'iPad' or brend == 'iPhone':
                    brend = 'Apple'
                elif brend == 'iPad' or brend == 'iPhone' or brend == 'Home':
                    brend = 'Apple'
                elif  brend == 'iPad' or brend == 'iPhone' or brend == 'Home':
                    brend = 'Apple'
       
                if corect_model(model):
                    model  = corect_model(model) 
                for text in word_replace:
                    if text[0] in t_clear:
                        cl_t = t_clear.replace(text[0], text[1])



                print("ПЕРЕДЗАПИСЬЮ", model)
                brend_wr, created  = SmartfonBrend.objects.get_or_create(brend = str(brend))
                model_wr, created  = SmartfonModels.objects.get_or_create(model =model.replace('Home ',''), brend_key = SmartfonBrend.objects.get(brend=str(brend)))
                part_wr = Spare_Part.objects.update_or_create(smartfonmodels = SmartfonModels.objects.get(model = model.replace('Home ','')),
                                                                action_problem_id = act_problem, 
                                                                name_service = 'Замена' +' ' + cl_t, 
                                                                available_part_id = available_part, 
                                                                quality_part_id = int(quality_part), 
                                                                repair_place_id = int(repair_place),
                                                                popular_service = False, 
                                                                base_prise = int(price),
                                                                description_service = deskript,
                                                                image_part_base = img,
                                                                )
 

                with open(img_sm_device + "font/" + 'name.txt', "a") as name_file: # данные - выборка и запись
                    name_file.write("Запись в БД прошла успешно" + '\n' )
                 
                name_file.close() 
        except Exception:
            print("ПРОПУСКАЮ из за ошибки")
            pass 

    image_rebild()                                     
    print("СКРИПТ ЗАВЕРШЕН УСПЕР")