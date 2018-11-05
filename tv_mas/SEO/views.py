from __future__ import unicode_literals
from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.shortcuts import render
from django.shortcuts import render_to_response
#from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from datetime import *
import random
import string
from django.http import HttpResponse
# Create your views here.
from SEO.models import Title_pape

