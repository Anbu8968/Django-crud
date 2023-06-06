from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from .models import user


class User(APIView):
    def post(self,request):
        data=request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added User",safe=False)
        else:
            return JsonResponse("Error")
    def get(self,request):
        user1=user.objects.all()
        serializer=UserSerializer(user1,many=True)
        if len(serializer.data)>0:
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse("No data",safe=False)
        # return HttpResponse("get")
    def put(self,request):
        data=request.data['email']
        user1=user.objects.get(email=data)
        serializer=UserSerializer(instance=user1,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({"Status":"updated successfully"})
    def delete(self,request):
        data=request.data['email']
        d=user.objects.get(email=data)
        d.delete()
        return JsonResponse({"status":"Delete"})