from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UseForm(UserCreationForm):
<<<<<<< HEAD
    email = forms.EmailField(label="이메일")
=======
    email = fomrs.EmailField(label="이메일")
>>>>>>> 30b9d28800fdd86d54464482e6df5fefbae708de

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")