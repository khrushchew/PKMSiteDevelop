from django.contrib.admin import AdminSite
from .models import NTZCompany

class NTZAdminSite(AdminSite):
    pass
ntz_admin_site = NTZAdminSite(name='ntz_admin')

ntz_admin_site.register(NTZCompany)