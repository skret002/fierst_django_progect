"""tv_mas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^skret002/', admin.site.urls),

    url(r'^', include ('accounts.urls')),
    url(r'^', include ('main.urls')),
    url(r'^', include ('suvenirka_order.urls')),
    url(r'^', include ('suvenirka_product.urls')),
    url(r'^', include ('suvenirka_order.urls')),
    url(r'^', include ('repair_tv.urls', namespace='tv_repair')),
    url(r'^', include ('smartfon.urls', namespace='smartfon')),
    url(r'^', include ('notebook.urls', namespace='notebook')),
    url(r'^', include ('photo.urls', namespace='photo')),
    url(r'^', include ('just_print_photo.urls', namespace='just_print_photo')),
    url(r'^', include ('print_documents.urls', namespace='print_documents')),
    url(r'^', include ('refcartridges.urls', namespace='refcartridges')),
    url(r'^summernote/', include ('django_summernote.urls')),

]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]