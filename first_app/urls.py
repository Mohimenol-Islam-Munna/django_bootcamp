from django.urls import path
from . import views



urlpatterns = [

    path('', views.employee),
    path('list/', views.employee_list)
]
