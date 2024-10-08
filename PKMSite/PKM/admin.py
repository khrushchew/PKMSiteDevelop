from django.contrib.admin import AdminSite
from .models import PKMCompany

class PKMAdminSite(AdminSite):
    pass

pkm_admin_site = PKMAdminSite(name='pkm_admin')

pkm_admin_site.register(PKMCompany)