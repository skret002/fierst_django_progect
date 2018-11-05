 # -*- coding: utf-8 -*-
import urllib2
import requests
from requests.exceptions import ConnectionError
from bs4 import  BeautifulSoup
import os, re
import shutil
from time import sleep
from random import randint
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

base_host = 'https://www.partsdirect.ru/search_by_models/'
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(ROOT_DIR, "templates","static", "media")
folder_img_parts = os.path.join(BASE_DIR, "img/",  "notebook/")

word_fall=[('наклейка'),('удлинитель'),('переходник'),('наклейки'),('набор винтов'),('переходник'),('резиновая ножка'),
                        ('переходник SATA'),('отвёртка'),('резиновая ножка'),]
word_repair_place = [('матрицы'),('экран'),('тачскрин'),('клавиатуры'),('жесткие диски и ssd'),('модули памяти'),
                      ('тачпады'),('вентиляторы'),('системы охлаждения'),]
replace_name = [('Матрица' , 'Матрицы'),('шлейф' , 'Шлейфа'),('клавиатура' , 'клавиатуры'),('Клавиатура' , 'Клавиатуры'),
                ('жесткий диск' , 'жесткого диска'),('оперативная память' , 'оперативной памяти'),('мультиконтроллер' , 'мультиконтроллера'),
                ('контроллер' , 'контроллера'),('флеш память' , 'флеш памяти'),('ШИМ-контроллер' , 'ШИМ-контроллера'),('видеочип' , 'видеочипа'),
                ('Видеочип' , 'видеочипа'),('северный мост' , 'северного моста'),('хаб' , 'хаба'),
                ('южный мост' , 'южного  моста'),('модуль' , 'модуля'),('стекло' , 'стекла'),('нижняя панель' , 'нижней панели'),
                ('нижняя часть' , 'нижней части'),('рамка матрицы' , 'рамки матрицы'),('топкейс' , 'топкейса'),
                ('Задняя крышка' , 'Задней крышки'),('динамики' , 'динамиков'),('левый динамик' , 'левого динамика'),('камера' , 'камеры'),
                ('Петля крышки' , 'Петли крышки'),('петля левая' , 'левой петли'),('нижняя часть' , 'нижней части'),('крышка матрицы' , 'крышки матрицы'),
                ('петля правая' , 'правой петли'),('петли крышки' , 'петель крышки'),('процессор' , 'процессора'),('' , ''),
                ('материнская плата' , 'материнской платы'),('плата для ноутбука' , 'платы для ноутбука'),
                ('вентилятор' , 'вентилятора'),('кулер' , 'кулера'),('шлейф матрицы' , 'шлейфа матрицы'),('разъем питания' , 'разъема питания'),
                ('разъем USB' , 'разъема USB'),('аккумулятор' , 'аккумулятора'),
                ('тачпад' , 'тачпада'),('антенна' , 'антенны'),(' разъем питания',' разъема питания')]
no_replace_name = [('Блок питания'),('аккумулятор'),]
def problem_name_service(name_part):   # определяем категорию 
    if  any(x in name_part for x in ['матрицы', 'тачскрин',]):
        ids = (9)#
    elif  any(x in name_part for x in ['клавиатуры',]):
        ids = (3)  #
    elif  any(x in name_part for x in ['блоки питания', 'аккумуляторы', 'блоки питания Apple',]):   
        ids = (16) #
    elif  any(x in name_part for x in ['жесткие диски и ssd','Жесткий диск']):    
        ids = (14) #
    elif  any(x in name_part for x in ['модули памяти',]):    
        ids = (17) #
    elif  any(x in name_part for x in ['микросхемы',]):   
        ids = (15) #
    elif  any(x in name_part for x in ['видеокарты', 'видеочипы',]): 
        ids = (8) #
    elif  any(x in name_part for x in ['мосты','мультиконтроллеры',]): 
        ids = (15) #
    elif  any(x in name_part for x in ['корпусные детали',]): 
        ids = (7) #
    elif  any(x in name_part for x in ['процессоры',]): 
        ids = (15) #
    elif  any(x in name_part for x in ['материнские платы',]): 
        ids = (1) #
    elif  any(x in name_part for x in ['допплаты',]): 
        ids = (1) #
    elif  any(x in name_part for x in ['шлейфы',]): 
        ids = (18) #  
    elif  any(x in name_part for x in ['разъемы питания',]):   
        ids = (6)  #
    elif  any(x in name_part for x in ['корпусные части',]): 
        ids = (7) #
    elif  any(x in name_part for x in ['подсветки и топ кейсы',]): 
        ids = (3)  
    elif  any(x in name_part for x in ['тачпады',]): 
        ids = (3) #
    elif  any(x in name_part for x in ['вентиляторы', 'системы охлаждения',]): 
        ids = (10) 
    else:
        ids = (19) # если нет в списке
    return(ids)




def image_rebild():
    directory = folder_img_parts
    files = os.listdir(directory)
    for file in files:
        try:
            base_im = Image.open(folder_img_parts + file)
            base_image = base_im.convert('RGB')
            draw = ImageDraw.Draw(base_image)
            width = base_image.size[0] #Определяем ширину картинки
            height = base_image.size[1] #Определяем высотукартинки
            if width == 400 and height == 400:
                font_size = 16
                width_center = 20
                    
            font_size = (height/23)
            width_center = (width- (width/110)*100)
            font = ImageFont.truetype(directory + "font/" +"RobotoCondensed-Bold.ttf", font_size)
            height_center = (height/15)
            color_text = 70, 130, 180
            draw.text((width_center,height_center, color_text),"тв-мастерская.рф",fill=color_text,font=font)
            base_image.save(directory + file)
        except IOError:
            pass

def get_html(url):
    try:
        response = urllib2.urlopen(url)
        response.encoding = 'UTF-8'
        response.close
        #sleep(randint(1,3))
        return response.read()
    except Exception:
        pass

def get_brend(html):
    soup  =  BeautifulSoup(html, 'html5lib')
    ul_brend = soup.find('ul', id='brand_list')
    brend_code = [item["data-id"] for item in ul_brend.find_all() if "data-id" in item.attrs]
    return(brend_code)

def get_model_url(code):
    payload = {'key': code} #code
    r = requests.post("https://www.partsdirect.ru/search_models_new.php", data=payload)
    resp = r.json()
    return(resp)

def clear_model_url():
    code_model = get_brend(get_html(base_host))
    for code_m in code_model:
        code = '21663:' + '1319' #str(code_m)
    return(code_m)  # все модели и их url 

def pars_url_parts(url):
    parts_url_and_catg =[]
    html = get_html(url)
    try:
        soup  =  BeautifulSoup(html, 'html5lib')
        result = soup.find('div', class_="results")

        pars_url = result.find_all('a', href=True)
        for u in pars_url:
            ht = get_html('https://www.partsdirect.ru' + u['href'])
            soup  =  BeautifulSoup(ht, 'html5lib')
            tr = soup.find_all('tr')
            for item in tr:
                full_url_part = item.find('td').find('a', href=True)['href']
                parts_url_and_catg.append({#'category':item.text,
                                        'url':'https://www.partsdirect.ru'+full_url_part})
    except(AttributeError, TypeError):
        pass
    return(parts_url_and_catg)
    

def data_part(part_url):
    clear_data = []
    html = get_html(part_url)
    soup  =  BeautifulSoup(html, 'html5lib')
    try:
        img = soup.find('span', class_="base").next["src"] #получаем ссылку на картинку
        write = requests.get(img, stream = True)
        img_name = img.split('/')[-1]
        image_paf =  (folder_img_parts + img_name)
    except(AttributeError, ConnectionError):
        image_paf = str(folder_img_parts + "text/" + 'no_im.png')

    clear_data.append({'image_local': image_paf,})
    try:
        with open(image_paf, 'wb') as out_file:
            shutil.copyfileobj(write.raw, out_file)
            del write 
    except(UnboundLocalError):
        pass
    model = soup.find('div', class_="w-comp").text
    clear_data.append({'model':model.replace('гарантируем 100% совместимость с ', '')})
    category = soup.find('ul', class_="path").find_all('li')
    clear_data.append({'category':category[-1].text})
    title = soup.find('div', class_="title").find('h1').text
    price = soup.find('div', class_="base-price").find('strong').text
    c_price= re.findall(r'([0-9]+)', price)
    
    clear_data.append({'title':title,
                       'c_price':(int(c_price[0])),
                        })

    availability_all = soup.find_all('div', class_="itm")
    for i in availability_all[0:2]:
        av_string = i.find('b').text
        av_int = re.findall(r'([0-9]+)', av_string)
        clear_data.append({'availability_now':(int(av_int[0]))})
    for i in availability_all[2:3]:
        av_string = i.find('b').text
        av_int = re.findall(r'([0-9]+)', av_string)
        clear_data.append({'availability_cache':(int(av_int[0]))})


    return(clear_data)
        


if __name__ == '__main__':
    main()



# исправить все со строки 61