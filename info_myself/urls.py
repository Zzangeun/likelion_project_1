from django.contrib import admin
from django.urls import path
from info_myself import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/post/<int:post_id>/', views.detail, name='detail'),
    path('home/post/new/', views.post_new, name='new'),
]
