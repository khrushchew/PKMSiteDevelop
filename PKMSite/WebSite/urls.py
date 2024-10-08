from django.urls import path, include
from .views import main

urlpatterns=[
    path('', main, name='main'),
    path('accounts/', include('django.contrib.auth.urls'))
]