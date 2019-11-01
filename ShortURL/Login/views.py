from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/msurl")
    else:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/msurl")
            else:
                return render(request, "LoginTemp/login.html") #Возвращает, если такого пользователя не существует
        else:
            return render(request, "LoginTemp/login.html")
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return HttpResponseRedirect("/login")
    else:
        return HttpResponseRedirect("/login")
