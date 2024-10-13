from django.contrib import admin
from ..models.Department import Department


class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'field', 'indent') 
    readonly_fields = ('company',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(company__code=request.user.username)


admin.site.register(Department, FieldAdmin)