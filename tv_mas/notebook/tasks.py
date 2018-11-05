# -*- coding: utf-8 -*-
from celery.task import task
from celery.schedules import crontab
from tv_mas.celery_app import app
from models import *
from .parts_derect import *
import time
import re

__autor__ = 'mevlutov'


@app.task
def main():
    data = []
    brend_code =  get_brend(get_html(base_host))    
    model_url=[]
    parts = []
    part_url = list()
    for brend in brend_code:   # на время тестов
        resp_json = get_model_url('21663:' + str(brend))            # код каждого бренда для получения json
        for url in resp_json['tips']:
            model_url.append(url['url'])
            print('FIERST STADY', url['url'])
    try:
        for url in model_url:
            parts_url = pars_url_parts('https://www.partsdirect.ru' + url)
            parts.append(parts_url)
            print('PRE SECOND STADY', parts_url)
    except Exception:
        print("Пропустил")
    print('START SECOND STADY', parts)
    x = len(parts)
    print(x)
    for cycle in  range(0, x):
        for u in parts[cycle]:
            part_url.append(u['url'])#    for case in part_url:
    for case in part_url:
        try:
            data_case = data_part(case)
            if  any(x in data_case[3]['title'] for x in word_fall):
                pass
            else:
                brend_m= (data_case[1]['model']).split(' ')
                brend = brend_m[0]
                model = data_case[1]['model']
                category = (data_case[2]['category'])
                act_problem = problem_name_service(category)
                if  any(x in data_case[3]['title'] for x in no_replace_name):
                    name_part = data_case[3]['title']
                else:
                    name_part = (data_case[3]['title'] + 'c заменой')
                if int(data_case[4]['availability_now']) >1 or int(data_case[5]['availability_now']) > 1: 
                    available_part = 1
                elif int(data_case[4]['availability_now']) == 0 and int(data_case[5]['availability_now']) == 0 and int(data_case[6]['availability_cache']) > 1:
                    available_part = 2
                else:
                    available_part = 3
                quality_part = 1
                if any(m in data_case[2]['category'] for m in word_repair_place):
                    repair_place = 2
                else:
                    repair_place = 1 
                price =  data_case[3]['c_price']
                deskript = (name_part + ' ' + ' в нашем сервисе - это 3 месяца железной гарантии, квалифицированные мастера и разумные цены!')
                img = data_case[0]['image_local']


                brend_wr, created  = NotebookBrend.objects.get_or_create(brend = str(brend))
                model_wr, created  = NotebookModels.objects.get_or_create(model =model, brend_key = NotebookBrend.objects.get(brend=str(brend)))
                part_wr = Spare_Part.objects.update_or_create(notebookmodels = NotebookModels.objects.get(model = model),
                                                                action_problem_id = act_problem, 
                                                                name_service =  str(name_part), 
                                                                available_part_id = available_part, 
                                                                quality_part_id = int(quality_part), 
                                                                repair_place_id = int(repair_place),
                                                                popular_service = False, 
                                                                base_prise = int(price),
                                                                description_service = deskript,
                                                                image_part_base = img,
                                                                )
        except Exception:
            print("Была фатальная ошибка")
    image_rebild()
    print("СКРИПТ ЗАВЕРШЕН")