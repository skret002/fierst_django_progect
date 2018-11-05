from django.conf.urls import url, include
from django.contrib import admin
from . import views
 
urlpatterns =  [
    
    url(r'suvenirka/page/(\d+)/$', views.all_suvenirka_product, name='all_suvenirka_product'),

    url(r'suvenirka/suvenirka.html', views.suvenirka_home, name='suvenirka_home'),

    url(r'suvenirka/krugka_product.html', views.krugka_product, name='krugka_product.html'), #1

    url(r'suvenirka/chehlu_product.html', views.chehlu_product, name='chehlu_product.html'),

    url(r'suvenirka/futbolki_product.html', views.futbolki_product, name='futbolki_product'),

    url(r'suvenirka/tarelki_product.html', views.tarelki_product, name='tarelki_product'),

    url(r'suvenirka/watch_product.html', views.watch_product, name='watch_product'),

    url(r'suvenirka/pazlu_product.html', views.pazlu_product, name='pazlu_product'),

    url(r'suvenirka/kalendari_product.html', views.kalendari_product, name='kalendari_product'),

    url(r'suvenirka/podushki_product.html', views.podushki_product, name='podushki_product'),

    url(r'suvenirka/magnitu_product.html', views.magnitu_product, name='magnitu_product'), 
    
    url(r'suvenirka/poster_product.html', views.poster_product, name='poster_product'), 
    
    url(r'suvenirka/bs_fl.html', views.bs_fl_product, name='bs_fl_product'), 

    url(r'suvenirka/nabor_product.html', views.nabor_product, name='nabor_product'), 

    url(r'suvenirka/meshki_product.html', views.meshki_product, name='meshki_product'), # 13

    url(r'suvenirka/drugie_product.html', views.drugie_product, name='drugie_product'), # 14

    url(r'suvenirka/pano_product.html', views.pano_product, name='pano_product'), # 15

    url(r'suvenirka/holst_product.html', views.holst_product, name='holst_product'), # 16

    url(r'suvenirka/sumki_i_obuv_product.html', views.sumki_i_obuv_product, name='sumki_i_obuv_product'), # 17

    url(r'suvenirka/kalendari_product.html', views.kalendari_product, name='kalendari_product'), # 18

    url(r'suvenirka/kolaj_na_holste_product.html', views.kolaj_na_holste_product, name='kolaj_na_holste_product'), # 19

    url(r'suvenirka/shirokofor_pechat.html', views.shirokofor_pechat, name='shirokofor_pechat'), # 20
    
    url(r'suvenirka/r_kartin.html', views.r_kartin, name='r_kartin'), # 21

    url(r'suvenirka/domovue_znaki.html', views.domovue_znaki, name='domovue_znaki'), # 22

    url(r'suvenirka/info_znaki.html', views.info_znaki, name='info_znaki'), # 23

    url(r'suvenirka/tablichki_plastik.html', views.tablichki_plastik, name='tablichki_plastik'), # 24

    url(r'suvenirka/tablichki_fsk.html', views.tablichki_fsk, name='tablichki_fsk'), # 25

    url(r'suvenirka/teh_tablichki.html', views.teh_tablichki, name='teh_tablichki'), # 26

    url(r'suvenirka/neft_gaz.html', views.neft_gaz, name='neft_gaz'), # 27
    
    url(r'suvenirka/jd_dorogi.html', views.jd_dorogi, name='jd_dorogi.html'), # 28

    url(r'suvenirka/portret_pamyatnik.html', views.portret_pamyatnik, name='portret_pamyatnik'), # 29

    url(r'suvenirka/ritualnue_tablichki.html', views.ritualnue_tablichki, name='ritualnue_tablichki'), # 30

    url(r'suvenirka/kompozicii.html', views.kompozicii, name='kompozicii'), # 31

    url(r'suvenirka/graf_kompozicii.html', views.graf_kompozicii, name='graf_kompozicii'), # 32

    url(r'suvenirka/arki_kompozicii.html', views.arki_kompozicii, name='arki_kompozicii'), # 33

    url(r'suvenirka/keramika_izo.html', views.keramika_izo, name='keramika_izo'), # 34

    url(r'suvenirka/gold_arnamentu.html', views.gold_arnamentu, name='gold_arnamentu'), # 35

    url(r'suvenirka/metal_photo.html', views.metal_photo, name='metal_photo'), # 36

    url(r'suvenirka/grafiti.html', views.grafiti, name='grafiti'), # 37

    url(r'suvenirka/portretu_pod_jivopis.html', views.portretu_pod_jivopis, name='portretu_pod_jivopis'), # 38

    url(r'suvenirka/foto_na_stekle.html', views.foto_na_stekle, name='foto_na_stekle'),

    url(r'^suvenirka/list_produkts/(?P<list_produkts_id>\w+)/$', views.product, name='list_produkts'),

    url(r'^suvenirka/list_categoris/(?P<list_categoris_id>\w+)/$', views.product, name='list_categoris'),

    url(r'^suvenirka/list_produkts/(?P<list_produkts_id>\w+)/$', views.product, name='product'),

    url(r'^suvenirka/list_produkts/(?P<list_produkts_id>\w+)/$', views.product, name='products_color'),
]