from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "foodApp"

urlpatterns = [
  path('', views.load, name = "get")
]

