from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.
def print(request):
    return HttpResponse("Hello World")
def home(request):
    return HttpResponse("Hi")