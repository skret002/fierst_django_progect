# -*- coding: utf-8 -*-
import urllib2
from bs4 import  BeautifulSoup
import re
import time
from repair_tv.models import *


BASE_URL = 'http://remont-aud.net/forum/61-0-'

def get_html_rem_aud(url):
    response = urllib2.urlopen(url)
    response.encoding = 'UTF-8'
    return response.read()



def page_count_rem_aud(html):
	soup  =  BeautifulSoup(html, 'html5lib')
	pagination = soup.find_all('a', class_='switchDigit')[-1].text
	return int(pagination)


def parse_rem_aud(html):
    soup  =  BeautifulSoup(html, 'html5lib')
    table = soup.find('table', class_='gTable')

    models  = []
    time.sleep(5)
    for row in table.find_all('tr')[6:]:
 	try:
 			a = row.find('a', class_='threadLink').text
            
 	except AttributeError:
 			pass
        brend = a.split()[0].strip()
        a = re.sub(r'\([^\)]+\)', '', a)
        models.append({
           'name': a,
           'brend': brend
        })
    Tv_Write_Info = Tv_Models.objects.update_or_create(
                        number_tv_model=models[0]['name'],
                    is_brend = BrendTv.objects.get_or_create(brend=models[0]['brend'],)[0]
                                                   )
    for model in models:
        print model

    return models



#def main_rem_aud():
#	pages = page_count(get_html(BASE_URL))
#	print pages
#	models  = []
#	for p in range(1, pages + 1):
#        time.sleep(5)  #  что бы не уронить жертву
#		models.extend(parse(get_html(BASE_URL + str(p))))
#		print(BASE_URL + str(p))
#	print(len(models))




if __name__ == '__main__':
    main()
