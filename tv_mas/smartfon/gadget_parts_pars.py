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
reload(sys)
sys.setdefaultencoding('utf-8')


#from repair_tv.models import *



BASE_URL = 'http://www.gadgetparts.ru/catalog/?page_18='
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(ROOT_DIR, "templates","static", "media")
img_sm_device = os.path.join(BASE_DIR, "img/",  "smartfonu/")
base_host = 'http://www.gadgetparts.ru'


request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://thewebsite.com",
        "Connection": "keep-alive" 
    }

word_replace = [('Антенна' , 'Антенны'),
                ('Аудио коннектор' , 'Аудио коннектора( не работают наушники)'),
                ('Аудио шлейф' , 'Аудио шлейфа'),
                ('Верхний', 'Верхнего'),
                ('Вибромотор' , 'Вибромотора'),
                ('Голосовой шлейф' , 'Голосового шлейфа'),
                ('Дисплей' , 'Дисплея'),
                ('Задняя камера ' , 'Задней камеры '),
                ('Задняя крышка' , 'Задней крышки (корпуса)'),
                ('Камера' , 'Камеры'),
                ('Кнопка вибро' , 'Кнопки вибро' ),
                ('Кнопка включения' , 'Кнопки включения' ),
                ('Кнопка громкости' , 'Кнопки громкости'),
                ('Кнопка Hоme' , 'Кнопки Hоme' ),
                ('Коннектор' , 'Коннектора'),
                ('Контроллер' , 'Контроллера'),
                ('Крепеж' , 'Крепежа'),
                ('Микросхема контроллер' , 'Микросхемы контроллера'),
                ('Микросхема' , 'Микросхемы'),
                ('Модуль' , 'Модуля'),
                ('дисплей' , 'дисплея'),
                ('тачскрин' , 'тачскрина'),
                ('Зтачскринаа' , 'тачскрина'),
                ('Зтачскрина' , 'тачскрина'),
                ('Модуль' , 'Модуля'),
                ('Микросхема' , 'Микросхемы'),
                ('рамка' , 'рамки'),
                ('Нижний порт' , 'Нижнего порта'),
                ('Нижний шлейф' , 'Нижнего шлейфа'),
                ('Передняя камера' , 'Передней камеры'),
                ('Полифонический блок' , 'Полифонического блока'),
                ('Сенсорное стекло' , 'Сенсорного стекла' ),
                ('тачскрин' , 'тачскрина'),
                ('Слуховой динамик' , 'Слухового динамика'),
                ('Стекло' , 'Стекла'),
                ('Тачпад' , 'Тачпада'),
                ('Шлейф' , 'Шлейфа'),
                ('Усилитель' , 'Усилителя'),
                ('Сим-лоток' , 'Сим-лотока'),
                ('Рамка' , 'Рамки' ),
                ('Разъем' , 'Разъема'),
                ('Подсветка дисплея' , 'Подсветки дисплея'),
                ('Переходник шлейфа' , 'Переходника шлейфа' ),
                ('Передняя камера' , 'Передней камеры' ),
                ('Основной шлейф' , 'Основного шлейфа'),
                ('Нижняя плата' , 'Нижней платы (если не заряжается)'),
                ('Нижний системный разъем' , 'Нижнего системного  разъема'),
                ('Нижний порт зарядки' , 'порта зарядки'),
                ('Матрица' , 'Матрицы'),
                ('Крышка дисплея' , 'Крышки дисплея' ),
                ('Кнопка' , 'Кнопки'),
                ('Клавиатура' , 'Клавиатуры'),
                ('Верхний аудио шлейф' , 'Верхнего аудио шлейфа( не слышите собеседника, не работают датчики)'),
                ('Антенна Wi-Fi' , 'Антенны Wi-Fi ( если плохо ловит wifi) '),
                ('Аккумулятор' , 'Аккумулятора'),]


word_delete = [('Карта'),
                ('Клей, герметик'), ('Кольцо на кнопку'),
                ('Коробка'),('Матрица для ноутбука'),('Набор винтов'),('Набор инструментов'),
                ('Набор кнопок'),('Набор крепежно-прижимных'),('Накладка на аудио '),
                ('Наклейка'), ('Наклейки'),('Переходник шлейфа'),('Присоска вакуумная'),
                ('Прозрачный двухсторонний'),('Разъем сим карты '),('Рамка под сенсорное стекло'),
                ('Резинка под кнопку'),('Сим-лоток iPhone'), ('Скотч 3M'),('Скрепка'),
                ('Трафарет'),('Уплотнитель'),('Сеточка'),('Резинка'),('Прозрачный двухсторонний'),
                ('Присоска вакуумная'),('Переходник Lightning-Jack 3.5 '),('Отвертка'),('Нижние винты'),
                ('Наклейки для сборки'),('Наклейка'),('Накладка'),('Набор крепежно-прижимных'),
                ('Набор кнопок'),('Набор инструментов'),('Набор винтов'),('Набор боковых кнопок'),('Крепеж'),('Кольцо на кнопку'),('Клей, герметик') ,
                ('Карта винтов '),('Инструмент'),('Водозащитная проклейка'),('Чехол-накладка,'),('Belkin'),('USB iPhone'),('USB Lightning'),
                ('USB iPhone'),('Автодержатель'),('Android'),('3D'),('противоударное'),
                ('Автомобильное '),('Блок зарядки'),('кабель micro USB'),('Защитное противоударное '),('12w'),
                ('Наушники'),('Чехол'),('Silicon'),('Case'),('Чехол'),('8 GB пустая iPhone 3G ')]

word_another_group = [('Автомобильное зарядное'),
                        ('Защитная пленка') ,
                        ('Защитное противоударное'),
                        ('Инструмент') ,
                        ('Отвертка') ,
                        ('USB кабель'),
                        ('Чехол'),
                        ('Очиститель-спрей'),
                        ('Наушники') ,
                        ('Коробка') ,
                        ('Комплект сеточек'),
                        ('Комплект защиты'),
                        ('Кабель') ,
                        ('Защитное противоударное'),
                        ('Защитная'),
                        ('Блок питания'),
                        ('Блок зарядки') ,
                        ('Беспроводные'),
                        ('Автомобильное'),
                        ('Автодержатель'),
                        ('Автоадаптер'),]
word_original = [('Оригинал'),
                ('оригинал'),
                ('Оригинальный'),
                ('оригинальный'),
                ('original'),]
word_repair_place = [('Антенны'),
                    ('Аудио шлейфа'),
                    ('Замена Верхнего'),
                    ('Вибромотора'),
                    ('Голосового'),
                    ('Дисплея'),
                    ('Задней камеры'),
                    ('Задней крышки'),
                    ('Камеры'),
                    ('вибро'),
                    ('Кнопки'),
                    ('Модуля'),
                    ('дисплея'),
                    ('тачскрина'),
                    ('Нижнего шлейфа'),
                    ('Передней камеры'),
                    ('Полифонического блока'),
                    ('Сенсорного стекла'),
                    ('тачскрина'),
                    ('Слухового динамика'),
                    ('Шлейфа'),
                    ('Передней камеры'),
                    ('Основного шлейфа'),
                    ('Нижней платы'),
                    ('Матрицы'),
                    ('Крышки дисплея'),
                    ('Верхнего аудио шлейфа'),
                    ('Антенны Wi-Fi'),
                    ('Аккумулятора'),]

word_replace_in_name = [('Wi-Fi'),('wifi'),('Power'),('Volume'),
                        ('Mute'),('White'),('Black'),('Gold'),
                        ('Silver'),('Rose'),('gold'),('Space Gray'),
                        ('Black'),('Rose'),('gold'),('Red'),
                        ('Hоme'),('GPS'),('Wi-Fi'),('wifi'),
                        ('NFC'),('U2'),('1608А2'),('PM8019'),
                        ('Wi'),('Fi'),('PM8018'),('1608A1'),
                        ('GSM'),('Apple2'),('32'),('16'),
                        ('Apple2'),
                        ('Space'),('HQ'),('Matte'),('gray'),('Home '),
                        ('bluetooth'),('U2, 1610А1 '),('GB'),('Blue'),
                        ('Dark'),('Green'),('Pink'),('Jet'),
                        ('610A3B '),('10 3 '),('U2,1610А3 '),('bluetooth'),('blue'),('3G '),(' Orange'),
                        (' Silicon'),(' Premium'),(' Baseus'),(' Purple'),(' Yellow'),(' Purple'),
                        (' Purple'),(' Orange'),('OTG'),('tooth'),('Micro'),('mute '),]



apple_detect = [('iPad'),('iPhone'),('Apple'),('MacBook'),('iPod')]

akb = [('Аккумулятор'),('аккумулятор'),('Аккумулятор'),('АКБ'),('акб'),('аккумулятор'),]

lcd = [('Модуль '),('дисплей'),('тачскрин'),('Модул'),('Дисплей'),('Тачскрин'),('тачскрин'),('Дисплей'),('Модуль')
        ,('дисплей'),('Сенсорное стекло'),('Стекло'),('Матрица'),]

wi = [('Антенна'),('Антенна Wi-Fi'),('Усилитель'),('антенна')]

korpus = [('Задняя крышка'),('корпуса'),('Корпус'),('корпус'),('Корпуса')]

  ###Корекция моделей iPHONE 
ipad2=[('iPad 2 2'),('iPad 2 3G'), ('3G iPad 2'),
        ('iPad 2 3'),('iPad2'),('iPad 2 1'),]

iPhone6=[('iPhone 6 iPhone'),('iPhone 6 6')]

iPad3_4=[('iPad 3 3G'),('iPad 3'),('iPad 4'),
            ('iPad 4 3G'),]

iPad_mini = [('iPad mini 3G'),('iPad mini mini'),('iPad Mini')]

iPhone5=[('iPhone 5G'),('iPhone 5 iPhone'),('iPhone 5 Plum'),('iPhone 5 Orange')]

iPhone5S=[('iPhone 5S iPhone'),('iPhone 5 5S'),
            ('iPhone 5S SE'),('iPhone 5 5S'),('iPhone SE'),('iPhone 5S Purple'),
            ('101 iPhone 5S')]

iPhone6S=[('iPhone 6S iPhone'),]

iPad_5_Air=[('3G iPad 5'),('mute iPad 5')]

iPhone_6_Plus=[('iPhone 6 6Plus'),('103 iPhone 6S')]

iPhone_7=[('iPhone 7 7'),]

iPhone_4S=[('iPhone 4 4S'),('iPhone 4S C'),]
iPhone_5C=[('iPhone 5C Yellow'),]

def corect_model(text):
    if any(m in text for m in ipad2):
        model = 'iPad 2' 
    elif any(m in text for m in iPad3_4):
        model = 'iPad 3 4' 
    elif any(m in text for m in iPad_mini):
        model = 'iPad mini' 
    elif any(m in text for m in iPhone6):
        model = 'iPhone 6'
    elif any(m in text for m in iPhone5):
        model = 'iPhone 5' 
    elif any(m in text for m in iPhone5S):
        model = 'iPhone 5S'    
    elif any(m in text for m in iPhone6S):
        model = 'iPhone 6S'    
    elif any(m in text for m in iPad_5_Air):
        model = 'iPad 5 Air'
    elif any(m in text for m in iPhone_7):
        model = 'iPhone 7'
    elif any(m in text for m in iPhone_4S):
        model = 'iPhone 4S'
    elif text == 'iPhone Plus':
        model = 'iPhone 8 Plus'
    elif text == 'iPhone':
        model = 'iPhone 8'
    elif any(m in text for m in iPhone_5C):
        model = 'iPhone 5C'
    else:
        model = text
    return(model)

def problem_name_service(name_part):   # определяем категорию 
    if any(ak in name_part for ak in akb):
        ids = (31)
    if any(w in name_part for w in wi):
        ids = (30)
    if any(k in name_part for k in korpus):
        ids = (28)

    if  ('Аудио коннектор' in name_part):
        ids = (16)
    if  ('Аудио шлейф' in name_part):
        ids = (14)        
    if  ('Верхний' in name_part):
        ids = (8)   
    if  ('Вибромотор' in name_part or 'Кнопка вибро' in name_part):
        ids = (10)
    if  ('Голосовой шлейф' in name_part):
        ids = (5)   
    if any(x in name_part for x in lcd):
        ids = (29)
 
    if  ('Задняя камера' in name_part  or 'Камера'  in name_part or 'Передняя камера' in name_part ):
        ids = (17)    
    if  ('Кнопка' in name_part or 'Клавиатура' in name_part or 'Кнопка включения' in name_part):
        ids = (6)   
    if  ('Коннектор' in name_part or 'Контроллер' in name_part or 'Микросхема'  in name_part):
        ids = (31)  
    if  ('Нижний порт' in name_part or 'Нижний шлейф' in name_part or 'Разъем' in name_part or 'Нижняя плата' in name_part or 'Нижний системный разъем' in name_part or 'Нижний порт зарядки' in name_part):
        ids = (31)  

    if  ('Сим-лоток' in name_part):
        ids = (12)  
    if  ('Слуховой динамик' in name_part or 'Полифонический блок' in name_part):
        ids = (8)  
    if  ('Верхний аудио шлейф' in name_part): 
        ids = (8)  
 
    if  ('Крепеж' in name_part or 'Подсветка дисплея' in name_part or 'Рамка' in name_part):
        ids = (29)  
    if  ('Шлейф' in name_part):
        ids = (31)  
    if  ('Крышка дисплея' in name_part or 'Тачпад' in name_part or 'Основной шлейф' in name_part or 'Переходник шлейфа' in name_part):
        ids = (27)  
    try:     
        return(ids)
    except UnboundLocalError:
        return(27)

def get_html_gadget(url):
    r = urllib2.Request(url, headers=request_headers)
    try:
        response = urllib2.urlopen(r, timeout = 100)
        if response.getcode() == 200:
            print(response.getcode())
            response.encoding = 'UTF-8'
            response.close
            return response.read()
        else:
            print(response.getcode(), 'Bad URL')
            sleep(randint(60,100))
            pass
    except urllib2.URLError:
        pass


def get_pages(html):
    soup  =  BeautifulSoup(html, 'html5lib')
    pagination = soup.find_all('a', class_='pagination__link')[-2].text

    return(int(pagination)) # возвращаем кол-во страниц


def get_part_url(html):
    soup  =  BeautifulSoup(html, 'html5lib')
    container_part = soup.find('div', class_='listing__container')
    cart_url = []
    for li_url in container_part.find_all('li'):
        for url in li_url.find_all('a', href=True):
            cart_url.append(url['href'])

    return(cart_url) # возвращаем все ссылки на карточки товара с одной странице


def info_part(html):
    data = []
    
    try:
        soup  =  BeautifulSoup(html, 'html5lib')
        product__title = soup.find_all('h1', class_='product__title')
        for t in  product__title:
            data.append({
                        'name_part': t.text})
        
        product__price = soup.find_all('div', class_='product__price')
        for s in product__price:
            data.append({
                        'price': s.find("span").text})
        try:
            count_part = soup.find(attrs={"data-id":"27"}).parent('div')
        except AttributeError:
            count_part = '0'
            
        for count in count_part:  #  получаем только с магаза с кодом 27
            try:
                c_str = count.text.replace(u' шт', '').replace('>', '').replace('<', '')
            except AttributeError:
                c_str = '0'
            try:
                c_int = int(c_str)
            except UnicodeEncodeError:
                c_int = 0
            data.append({
                        'count': c_int})

        data.append({
                    'product__description': soup.find('div', class_='product__description').text})

        # Дальше работаем с картинками
        try:
            img_div = soup.find('div', class_='product__image').next["src"]   # получаем ссылку на img
            write = requests.get(img_div, stream = True)
            img_name = soup.find('div', class_='product__code').text.replace('Артикул: ', '')
            image_paf =  (img_sm_device + img_name + '.png' ).replace('\n', '')
        except TypeError:
            image_paf = None
        data.append({
                        'image_local': image_paf})

        try:
            with open(image_paf, 'wb') as out_file:
                shutil.copyfileobj(write.raw, out_file)
                del write 
        except UnboundLocalError:
            pass
    except TypeError:
        pass
    
    
    return(data)


def image_rebild():
    directory = img_sm_device
    files = os.listdir(directory)
    for file in files:
        try:
            base_im = Image.open(img_sm_device + file)
            base_image = base_im.convert('RGBA')
            draw = ImageDraw.Draw(base_image)
            width = base_image.size[0] #Определяем ширину картинки
            height = base_image.size[1] #Определяем высотукартинки
            if width == 400 and height == 400:
                font_size = 16
                width_center = 20
                    
            font_size = (height/23)
            width_center = (width- (width/110)*100)
            font = ImageFont.truetype(img_sm_device + "font/" +"RobotoCondensed-Bold.ttf", font_size)
            height_center = (height/15)
            color_text = 70, 130, 180
            draw.text((width_center,height_center, color_text),"Комплектующие предоставлены партнером",fill=color_text,font=font)
            base_image.save(img_sm_device + file)
        except IOError:
            pass


if __name__ == '__main__':
    main()