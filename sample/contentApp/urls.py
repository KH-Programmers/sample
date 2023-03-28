from django.urls import path

from . import views

app_name = "contentsApp"
urlpatterns = [
    # ex: /polls/
    path('', views.indexView, name='index'),
    # ex: /polls/5/
    path('<int:content_id>/', views.contentView, name='content'),
    path('write/',views.writeView,name="write")
]