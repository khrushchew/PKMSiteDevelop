from django.urls import path, include
from .views import index, about, account, recovery, contact, CustomLoginView
from PKM.admin import pkm_admin_site
from NTZ.admin import ntz_admin_site

urlpatterns=[
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
    path('recovery/', recovery, name='recovery'),
    path('contact/', contact, name='contact'),
    # path('ntz/',ntz_admin_site.urls),
    # path('pkm/', pkm_admin_site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', CustomLoginView.as_view(), name='login')
]