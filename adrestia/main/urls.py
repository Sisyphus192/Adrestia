<<<<<<< HEAD
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='catalog'),
]
=======
#_*_coding:utf8_*_
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
>>>>>>> c1576a7f5719a41c452f0259c0981d0551017629
