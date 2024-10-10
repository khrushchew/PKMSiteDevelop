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

class CustomLoginView(LoginView):
    # def form_valid(self, form):

    #     user = form.get_user()

    #     if self.request.user.username == 'pkm':
    #         return redirect('/pkm/')
    #     elif self.request.user.get_username() == 'ntz':
    #         return redirect('/ntz/')
    #     else:
    #         return super().form_valid(form)


    def get_success_url(self):
        if self.request.user.username == 'pkm':
            return redirect('/pkm/')
        elif self.request.user.get_username() == 'ntz':
            return redirect('/ntz/')
        else:
            return super().get_success_url()
