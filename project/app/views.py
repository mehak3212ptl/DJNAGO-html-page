from django.shortcuts import render
from .models import *
from django.http import  HttpResponse
# Create your views here.
def register(request):
    return render(request,'register.html')

def registerdata(request):
    print(request.method)
    print(request.POST)

    