from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'list':'product-list/',
        'Detailed View':'/product-detail/<int:id>/',
        'Create':'product-create/',
        'Update':'product-update/<int:id>/',
        'Delete':'product-delete/<int:id>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewProduct(request,pk):
    product=Product.objects.get(id=pk)
    serializer=ProductSerializer(instance=product,many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# def createProduct(request):
#     d=request.data['name']
#     print(d,"name")
#     serializer=ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response("Added data")
#         # return Response(serializer.data)

#     else:
#         return Response("Error")

@api_view(['post'])
def createProduct(request):
    name=request.data['name']
    category=request.data['category']
    price=request.data['price']
    description=request.data['description']
    stars=request.data['stars']
    b=Product(name=name,category=category,price=price,description=description,stars=stars)
    b.save()
    return Response("Saved")
    
@api_view(['POST'])
def updateProduct(request,pk):
    product=Product.objects.get(id=pk)
    serializer=ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return Response("Items deleted Successfully")