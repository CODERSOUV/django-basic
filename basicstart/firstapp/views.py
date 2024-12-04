from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstapp(request):
    return render(request,'firstapp/new_app.html')

def about(request):
    return HttpResponse("Hello, Welcome to about page to my first app")

def contact(request):
    return HttpResponse("Hello, Welcome to contact page to my first app")