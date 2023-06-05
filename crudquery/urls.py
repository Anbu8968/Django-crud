from django.urls import path
from . import views

urlpatterns=[
    path('',views.show_all),
    path('product-create/',views.create_product),
    path('product-update/<int:pk>/',views.update_product),
    path('product-delete/<int:pk>/',views.delete_product)
]
