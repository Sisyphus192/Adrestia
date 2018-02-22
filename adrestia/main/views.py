from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Welcome")
