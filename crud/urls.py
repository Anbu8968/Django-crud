from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiOverview,name="apiOverview"),
    path('product-list/',views.ShowAll),
    path('product-detail/<int:pk>/',views.viewProduct),
    path('product-create/',views.createProduct),
    path('product-update/<int:pk>/',views.updateProduct),
    path('product-delete/<int:pk>/',views.deleteProduct)
]