from django.views.generic import ListView
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Courses
from .tables import CourseTable
import pandas as pd

# Create your views here.
def FCQloginpage(request):
    return render(request, 'main/FCQloginpage.html')

def course(request):
    table = CourseTable(Courses.objects.filter(crse=3170))
    return render(request, 'main/course.html', {'course':table})


#to pull create account page
def createAccount(request):
    return render(request, 'main/createAccount.html')
	
