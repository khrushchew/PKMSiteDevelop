from django.contrib import admin
from ...models.Company import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_paid', 'paid_machines_quantity', 'date_of_start', 'date_of_end', 'is_testdrive', 'number_of_support_staff')
    ordering = ('name', )

    def has_view_permission(self, request, obj=None):
        return request.user.username == 'admin'

    def has_add_permission(self, request):
        return request.user.username == 'admin'
    
    def has_change_permission(self, request, obj=None):
        return request.user.username == 'admin'
    
    def has_delete_permission(self, request, obj=None):
        return request.user.username == 'admin'


admin.site.register(Company, CompanyAdmin)