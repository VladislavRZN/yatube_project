from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("group/<slug>/", views.group_posts, name="group-posts"),
    # Главная страница
    path('', views.index),
] 
