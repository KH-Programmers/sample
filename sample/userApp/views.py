from django.http import HttpResponse
from django.urls import reverse
from mainApp import views
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from sample.forms import UserForm

def login(request):
    if request.method == "GET":
        return views.main(request, '', 'user/login')
    elif request.method =="post":
        username = request.post["username"]
        password = request.post["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
<<<<<<< Updated upstream
            login(request, user)
            return HttpResponse(reverse('mainApp:main'))
=======
            login_auth(request, user)
            return redirect('/')
>>>>>>> Stashed changes
        else:
            return views.main(request, '', 'user/login')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password) # 사용자 인증
            login(request, user) # 로그인
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form':form})