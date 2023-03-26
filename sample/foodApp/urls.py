from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "foodApp"

urlpatterns = [
  path('get/', views.load, name = "get")
]

