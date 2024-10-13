from django.contrib import admin
from ..models.Area import Area


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'indent', 'department')
    readonly_fields = ('indent', )
    ordering = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(department__field__company__code=request.user.username)
    

admin.site.register(Area, AreaAdmin)