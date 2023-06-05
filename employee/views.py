from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt 
def create(request):
    response=requests.get("http://127.0.0.1:8000/create/")
    if response.status_code==200:
        content=response.json()
        return HttpResponse("Succesfull")
    else:
        return HttpResponse("failed")
    # named =request.['name']
    # titled =request.POST['title']
    # emaild =request.POST['email']
    # newEmployee=Employee(name=named,title=titled,email=emaild)
    # newEmployee.save()
    # return HttpResponse("Employee Added")