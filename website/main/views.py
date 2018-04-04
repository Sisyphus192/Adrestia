from django.views.generic import ListView
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Courses
from .tables import CourseTable
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def course(request):
    table = CourseTable(Courses.objects.filter(subject='APPM'))
    return render(request, 'main/fcq_Natnael.html', {'course':table})
