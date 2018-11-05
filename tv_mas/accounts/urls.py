from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    #url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^log_all/$', views.login_all, name='login_all'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/profile/$', views.update_profile, name='update_profile'),
    url(r'^accounts/profile_view/$', views.view_profile, name='view_profile'),
]
