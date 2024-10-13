from django.contrib import admin
from ..models.Company import Company
from ..models.Field import Field


class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'company') 
    readonly_fields = ('company',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(company__name=request.user.username)

    def save_model(self, request, obj, form, change):
        company = Company.objects.get(name=request.user.username)
        obj.company = company
        super().save_model(request, obj, form, change)


admin.site.register(Field, FieldAdmin)
