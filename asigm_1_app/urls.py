from django.urls import re_path
from . import views

app_name='asigm_1_app'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    
    re_path(r'^(?P<person_id>[0-9]+)/$', views.detail, name = 'detail'),
    re_path(r'^details/(?P<person_id>[0-9]+)/$', views.detail, name='detail'),

    re_path(r'^add$', views.add, name='add'),
    re_path(r'^getAdd$', views.getAdd, name='getAdd'),

    re_path(r'^user$', views.user, name='user'),
    re_path(r'^useradd$', views.useradd, name='useradd'),

#     re_path(r'^$', views.IndexView.as_view(), name='index'),
#     re_path(r'^(?P<pk>[0-9]+)$', views.IndexView.as_view, name='detail')
 ]