from django.shortcuts import render
from .models import Person
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        "filter":"filter/",
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



