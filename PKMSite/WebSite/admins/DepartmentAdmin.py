from django.contrib import admin
from ..models.Department import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'field', 'indent', 'areas_quantity', 'machines_quantity', 'stuff_quantity') 
    readonly_fields = ('indent', 'areas_quantity', 'machines_quantity', 'stuff_quantity')

    ordering = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(field__company__code=request.user.username)


admin.site.register(Department, DepartmentAdmin)