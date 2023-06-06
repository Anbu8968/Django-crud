from django.urls import path
from . import views

urlpatterns=[
    path("",views.apiOverview,name="api overview"),
    path('age/',views.filter_by_awh,name="filter_by_age"),
    path('get-names/',views.get_names),
    path('create/',views.create_object),
    path('update/',views.update_person),
    path('values-col/',views.values_by_col)
]