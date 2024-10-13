from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def account(request):
    return render(request, 'account.html')

def recovery(request):
    return render(request, 'recovery.html')

def contact(request):
    return render(request, 'contact.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/admin/')  # Перенаправляем в админку
        else:
            messages.error(request, 'Неверный логин или пароль')
    
    return render(request, 'account.html')

