from django.contrib import admin
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


from PKM.admin import register_pkm_models
from NTZ.admin import register_ntz_models

def register_admin_models(admin_site, db_name):
    if db_name == 'pkm_db':
        register_pkm_models(admin_site)
    elif db_name == 'ntz_db':
        register_ntz_models(admin_site)

class CustomAdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        db_name = getattr(request, 'db_name', 'default')
        context['db_name'] = db_name
        return context

    def has_permission(self, request):
        register_admin_models(self, getattr(request, 'db_name', 'default'))
        return super().has_permission(request)

admin_site = CustomAdminSite(name='custom_admin')
