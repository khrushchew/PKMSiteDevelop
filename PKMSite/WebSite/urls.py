from django.urls import path, include
from .views import index, about, account, recovery, contact

urlpatterns=[
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
    path('recovery/', recovery, name='recovery'),
    path('contact/', contact, name='contact'),

]