from django.contrib import admin
from .models import PKMCompany
class YourPkmModelAdmin(admin.ModelAdmin):
    pass

def register_pkm_models(admin_site):
    admin_site.register(PKMCompany, YourPkmModelAdmin)

