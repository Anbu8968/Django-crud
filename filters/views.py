from django.shortcuts import render
from .models import Person
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        "filter":"filter-age/",
        "values":"values/",
        "value_list":"value-list/",
        "get":"get/",
        "aggregrate":"aggregrate/",
        "annotate":"annotate/",
        "bulk_create":"bulk-create/",
        "bulk update":"bulk-update/",
        "create":"create/",
        "update":"update/"
    }
    return Response(api_urls)


@api_view(['GET'])
def filter_by_awh(request):
    age=request.data['age']
    weight=request.data['weight']
    height=request.data['height']
    person=Person.objects.filter(age__gte=age,weight__gte=weight,height__gte=height)
    return Response(person)

@api_view(['GET'])
def values_by_col(request):
    col_name=request.data['col_names']
    col_values=Person.objects.values(col_name)
    if col_values:
        return Response(col_values)
    else:
        return Response("no data")

@api_view(['GET'])
def get_names(request):
    name=request.data['name']
    person=Person.objects.get(name=name)
    if person:
        return Response(person)
    else:
        return Response("No data")


@api_view(['GET'])
def create_object(request):
    name=request.data['name']
    age=request.data['age']
    weight=request.data['weight']
    height=request.data['height']
    person=Person.objects.create(name=name,age=age,weight=weight,height=height)
    return Response("Created")

@api_view(['GET'])
def update_person(request):
    name=request.data['name']
    age=request.data['age']
    weight=request.data['weight']
    height=request.data['height']
    person=Person.objects.filter(name=name).update(age=age,weight=weight,height=height)
    if person:
        return Response("Updated")
    else:
        return Response("no data find")

