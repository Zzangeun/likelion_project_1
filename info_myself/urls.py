from django.contrib import admin
from django.urls import path
from info_myself import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/post/my_infomation/', views.my_infomation, name='my_infomation'),
]
