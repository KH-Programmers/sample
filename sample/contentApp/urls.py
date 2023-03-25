from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.indexView, name='index'),
    # ex: /polls/5/
    path('<int:content_id>/', views.contentView, name='content'),
]