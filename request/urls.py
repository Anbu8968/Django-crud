from django.urls import path
from . import views
urlpatterns=[
    path('',views.get_request),
    path('post/',views.post_request),
    path('post-request/',views.post_request),
    path('env/',views.my_secret)
]