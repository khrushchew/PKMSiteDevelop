from django.contrib import admin
from ..models.Role import Role



class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

admin.site.register(Role, RoleAdmin)