from django.urls import path
from . import views

urlpatterns = [
    # Основная маска сайта ждёт любую переменную и перенесёт на страницу группировки постов
    path('group/<slug:slug>/', views.group_posts), 
    # Главная страница
    path('', views.index),
] 
