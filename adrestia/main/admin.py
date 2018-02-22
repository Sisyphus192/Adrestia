<<<<<<< HEAD
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls')),
]
=======
from django.contrib import admin
from .models import Question
admin.site.register(Question)
>>>>>>> c1576a7f5719a41c452f0259c0981d0551017629
# Register your models here.
