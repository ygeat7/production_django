from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/', views.machine_detail_page),
    path('', views.index)
]