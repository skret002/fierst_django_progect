# -*- coding: utf-8 -*-
from celery.task import task
from celery.schedules import crontab
from tv_mas.celery_app import app
from repair_tv.models import *
from .toshiba_parser import *
from .lg_parser import *
from .sony_parser import *
from .philips_parser import *
from .samsung_parser import *
from .rem_aud_pars import *
import time
import re

__autor__ = 'mevlutov'

@app.task
def main_toshiba():
    pages = get_page_count_toshiba()
    count_pages =  pages[0]
    count_pages_url = pages[1]

    for url in count_pages_url:
        time.sleep(5)  #  что бы не уронить жертву
        a=parse_toshiba(atach_url_toshiba + url)
        print(a)

@app.task
def main_rem_aud():
	pages = page_count_rem_aud(get_html_rem_aud(BASE_URL))
	print pages
	models  = []
	for p in range(1, pages + 1):
		models.extend(parse_rem_aud(get_html_rem_aud(BASE_URL + str(p))))
		print(BASE_URL + str(p))
	print(len(models))


    
@app.task
def main_sony():
    pages = get_page_count_sony()
    count_pages =  pages[0]
    count_pages_url = pages[1]
    
    for url in count_pages_url:
        print (atach_url_SONY + url)
        time.sleep(5)  #  что бы не уронить жертву
        a=parse_sony(atach_url_SONY + url)
        print(a)


@app.task
def main_lg():
    pages = get_page_count_lg()
    count_pages =  pages[0]
    count_pages_url = pages[1]

    for url in count_pages_url:
        time.sleep(5)  #  что бы не уронить жертву
        a=parse_lg(atach_url_LG + url)

@app.task
def main_samsung():
    pages = get_page_count_samsung()
    count_pages =  pages[0]
    count_pages_url = pages[1]

    for url in count_pages_url:
        time.sleep(5)  #  что бы не уронить жертву
        a=parse_samsung(atach_url_samsung + url)

@app.task
def main_philips():
    pages = get_page_count_philips()
    count_pages =  pages[0]
    count_pages_url = pages[1]

    for url in count_pages_url:
        time.sleep(5)  #  что бы не уронить жертву
        a=parse_philips(atach_url_philips + url)