from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import dummy
from django.conf import settings

@api_view(['GET'])
def my_secret(request):
    secret_key=settings.SECRET_KEY
    api_key=settings.API_KEY
    print(secret_key,"SECRET")
    print()
    print(api_key,"API_KEY")
    return Response("SEcret fetched")
@api_view(['GET'])
def get_request(request):
    response=requests.get("http://127.0.0.1:8000/api/product-list/")
    if response.status_code==200:
        data=response.json()
        print(data)
        return Response(data)
    else:
        return Response(response.status_code)
    
@api_view(['POST'])
def post_request(request):
    name=request.data['name']
    category=request.data['category']
    price=request.data['price']
    description=request.data['description']
    stars=request.data['stars']
    data={
        'name':name,
        'category':category,
        'price':price,
        'description':description,
        'stars':stars
    }
    response=requests.post("http://127.0.0.1:8000/api/product-create/",data=data)
    data1=response.json()
    print(data1)
    return Response(data1)



