from django.conf.urls import url
from . import views

urlpatterns = [
        #url(r'^$', views.index, name='index')
	path('', views.index, name='index'), #path to login page
#        re_path('', views.createAccount, name='createAccount') #link to create account
]
