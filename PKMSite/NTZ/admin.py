from django.contrib import admin
from .models import NTZCompany

class YourNtzModelAdmin(admin.ModelAdmin):
    pass

def register_ntz_models(admin_site):
    admin_site.register(NTZCompany, YourNtzModelAdmin)

