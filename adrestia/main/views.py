from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse


def index(request):
	return HttpResponse("<h2> Hey </h2>")
	

=======

# Create your views here.
from django.http import HttpResponse
 
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Welcome")
>>>>>>> c1576a7f5719a41c452f0259c0981d0551017629
