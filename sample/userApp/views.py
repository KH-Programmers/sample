from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as login_auth,get_user_model
from sample.forms import UserForm
from .models import Profile

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

    
def people(request, username): 
    person = get_object_or_404(get_user_model(), username=username)
    return render(request, 'user/people.html', {'person': person})