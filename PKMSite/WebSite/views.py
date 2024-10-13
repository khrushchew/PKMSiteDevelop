from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

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

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect



from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.username == 'pkm':
            return redirect('/pkm/')
        elif self.request.user.get_username() == 'ntz':
            return redirect('/ntz/')
        else:
            return super().get_success_url()