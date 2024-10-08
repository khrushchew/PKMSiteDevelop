from django.urls import path, include
from .views import main, CustomLoginView
from PKM.admin import pkm_admin_site
from NTZ.admin import ntz_admin_site

urlpatterns=[
    path('', main, name='main'),
    path('ntz/',ntz_admin_site.urls),
    path('pkm/', pkm_admin_site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', CustomLoginView.as_view(), name='login')
]