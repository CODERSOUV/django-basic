from django.http import HttpResponse
from django.shortcuts import render 
def home(request):
    # return HttpResponse("Hello, to the Home page")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello, to the about page")

def contact(request):
    return HttpResponse("Hello, to the contact page")
