# -*- coding: utf-8 -*-
import urllib2
import requests
from bs4 import  BeautifulSoup
import os, re
import shutil
import time
from repair_tv.models import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



BASE_URL_philips = 'http://www.repair-tv-philips.ru/models'
atach_url_philips = 'https://www.repair-tv-philips.ru'
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(ROOT_DIR, "templates","static", "media")
IMG_philips = os.path.join(BASE_DIR, "img/",  "philips/")
BREND_philips = "Philips"

def get_page_count_philips():
    response = requests.get(BASE_URL_philips).text
    soup  =  BeautifulSoup(response, 'html5lib')
    li     =  soup.find_all('li', class_='faemabold')

    page_count = []
    for links in li:
        liks_page=links.find('a', href=True)['href']
        page_count.append(liks_page)
    sum_pages =  len(page_count)
    #print sum_pages
    #for i in page_count:
    #    print i

    return sum_pages, page_count

def parse_philips(url):
    response = requests.get(url).text
    soup  =  BeautifulSoup(response, 'html5lib')
    name = soup.find_all('section', id='hlebniye-kroshki')
    try:
        description = soup.find('p', class_='opt-color-2').text
    except AttributeError:
        pass
    try:
        description_clear = description.replace('Москве', 'Санкт-Петербурге')
    except UnboundLocalError:
        description_clear = ' '
    
    
    model_info=[]

    for i in name:
        try:
            lis = i.find_all('li')[-1].text
        except AttributeError:
            pass


        model_info.append({
            'brend': BREND_philips,
            'name_models': lis.strip(),
            'descript':description_clear,

            })
    image = soup.find('div', class_='faemaleft-img opt-img-1')
    image_src =image.find('img').get('src')

    file_image = atach_url_philips+image_src
    r = requests.get(file_image, stream = True)
    cleare_lis = lis.replace(' ', '')  # чистим имя картинки от пробелов
    image_paf =  (IMG_philips + cleare_lis + '.jpg' ).replace('\n', '')
    model_info.append({
                        'image_local' : image_paf,
                      })
    try:
        with open(image_paf, 'wb') as out_file:
            shutil.copyfileobj(r.raw, out_file)
    except IOError:
        pass
    del r
    print model_info[0]['name_models']
    print model_info[0]['descript']
    print model_info[1]['image_local']
    Tv_Write_Info = Tv_Models.objects.update_or_create(number_tv_model=model_info[0]['name_models'],
                                                   info_model=model_info[0]['descript'],
                                                   model_photo=model_info[1]['image_local'],
                                                   is_brend = BrendTv.objects.get_or_create(brend=BREND_philips)[0]
                                                   )
#def main_philips():
#    pages = get_page_count_philips()
#    count_pages =  pages[0]
#    count_pages_url = pages[1]
#
#    for url in count_pages_url:
 #       time.sleep(5)  #  что бы не уронить жертву
#        a=parse_philips(atach_url + url)

if __name__ == '__main__':
    main()
