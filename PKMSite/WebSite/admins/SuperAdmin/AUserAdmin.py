from django.contrib.auth.models import User
from django.contrib import admin


class AUserAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.username == 'admin'

    def has_add_permission(self, request):
        return request.user.username == 'admin'
    
    def has_change_permission(self, request, obj=None):
        return request.user.username == 'admin'
    
    def has_delete_permission(self, request, obj=None):
        return request.user.username == 'admin'


admin.site.register(User, AUserAdmin)