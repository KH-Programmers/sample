from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

<<<<<<< HEAD
app_name = "userApp"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login')
=======
app_name = 'userApp'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup")
>>>>>>> 30b9d28800fdd86d54464482e6df5fefbae708de
]