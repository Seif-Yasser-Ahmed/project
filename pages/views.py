from django.shortcuts import render
from .models import Login
from django.shortcuts import HttpResponseRedirect
# Create your views here.

# 3laka ben request w response al server

# koll ma bt3ml fn btro7 t3mlha rabet alhoa url

# fn de m3naha saf7a


def index(request):
    return render(request, 'pages/index.html')


def about(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    data = Login(username=username, password=password)
    if data.is_valid():
        data.save()
    return render(request, 'pages/about.html')
