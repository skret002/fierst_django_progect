# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
# Create your views here.
from main.models import *



#def home(request):
   # top_text = Top_item.objects.all(),
   # a_text = Home_and_base.objects.all(),
    #footer_text = Footer_item.objects.all(),
    #return render(request,'base_home.html', locals());

#def title_home(request):
   # titles = Title_pape.objects.all(),
   # return render(request,'base_home.html', locals());
#def home(request):
    #top_text = Top_item.objects.all()
    #return render_to_response('base_home.html', {'top_text ':top_text})

def home(request):
    meta_home = Title_pape.objects.all()
    top_text = Top_item.objects.all()
    titles = Title_pape.objects.all() 
    a_text = Home_and_base.objects.all()
    return render_to_response('main/home.html', locals())
