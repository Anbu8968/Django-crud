from django.shortcuts import render
from django.db import connection

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import products

@api_view(['GET'])
def api_overview(request):
    api_urls={
        'list':'product-list/',
        'Detailed View':'/product-detail/<int:id>/',
        'Create':'product-create',
        'Update':'product-update/<int:id>/',
        'Delete':'product-delete/<int:id>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def show_all(request):
    cursor=connection.cursor()
    cursor.execute("select * from crudquery_products")
    a=cursor.fetchall()
    return Response(a)

@api_view(['POST'])
def create_product(request):
    name=request.data['name']
    category=request.data['category']
    price=request.data['price']
    description=request.data['description']
    stars=request.data['stars']
    query = f"INSERT INTO crudquery_products (name, category, price, description, stars) VALUES ('{name}', '{category}', {price}, '{description}', {stars});"
    with connection.cursor() as cursor:
        cursor.execute(query)
    return Response("successfully added")

@api_view(['POST'])
def update_product(request,pk):
    name=request.data['name']
    category=request.data['category']
    price=request.data['price']
    description=request.data['description']
    stars=request.data['stars']
    query = f"UPDATE crudquery_products SET"
    if name:
        query += f" name = '{name}',"
    if category:
        query += f" category = '{category}',"
    if price:
        query += f" price = {price},"
    if description:
        query += f" description = '{description}',"
    if stars:
        query += f" stars = {stars},"
    query = query.rstrip(',')  
    query += f" WHERE id = {pk};"
    with connection.cursor() as cursor:
        cursor.execute(query)
    
    return Response("Product updated successfully")


@api_view(['DELETE'])
def delete_product(request,pk):
    query=f'DELETE FROM crudquery_products WHERE id={pk};'
    with connection.cursor() as cursor:
        cursor.execute(query)
    return Response("Deleted")