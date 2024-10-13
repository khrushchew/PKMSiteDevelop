from django.urls import path, include
from .views import index, about, account, recovery, contact, login_view
from django.contrib import admin

urlpatterns=[
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('account/', login_view, name='account'),
    path('recovery/', recovery, name='recovery'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls)

]