from django.urls import path
from . import views

urlpatterns=[
    path("",views.print,name="print"),
    path("hi",views.home,name="home")
]