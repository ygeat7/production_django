from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_page),
    path('<str:pk>/', views.machine_detail_page),
    path('searchresult/', views.index), #검색결과 관련 함수 필요...   
]