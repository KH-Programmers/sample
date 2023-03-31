from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as login_auth
from sample.forms import UserForm

def login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    elif request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_auth(request, user)
            return redirect('/')
        else:
            return render(request, 'user/login.html')
    
    return HttpResponse("Hello World")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        email = request.POST["email"]
        user = authenticate(request, username=username, password=password)         
        if user is None:
            user = User.objects.create_user(username, email, password)
            return redirect('/user/login')
        else:
            return render(request, 'user/login.html') #커밋할파일
    else:
        return render(request, 'user/signup.html')