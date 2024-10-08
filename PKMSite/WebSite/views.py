from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# Create your views here.
def main(request):
    return render(request, 'default.html')


# views.py

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    def form_valid(self, form):
        # Получаем пользователя после успешного входа
        user = form.get_user()

        # Проверяем имя пользователя
        if self.request.user.username == 'pkm':
            return redirect('/pkm/')
        elif self.request.user.get_username() == 'ntz':
            return redirect('/ntz/')
        else:
            return super().form_valid(form)  # Стандартное поведение
