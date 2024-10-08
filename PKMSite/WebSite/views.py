from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# Create your views here.
def main(request):
    return render(request, 'default.html')
