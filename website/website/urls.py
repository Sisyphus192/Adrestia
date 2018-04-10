"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD:website/website/urls.py
from main.views import course, FCQloginpage, createAccount

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FCQloginpage),
    path('course/', course),
#    path('main/', include('main.urls')),
    path('createAccount/', createAccount)
=======
from main.views import course, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.login, name='login'),
    path('course/', course),
#    path('main/', include('main.urls')),
    path('signup/', signup, name='signup')
>>>>>>> 2de504f43a4cb4a778e0f93ec74189ef8dc1c01f:website/website/urls.py
#    path('admin/', admin.site.urls),
]

