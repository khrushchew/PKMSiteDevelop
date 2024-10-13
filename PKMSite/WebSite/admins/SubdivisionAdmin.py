from django.contrib import admin
from ..models.Subdivision import Subdivision


class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')
    ordering = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(area__department__field__company__code=request.user.username)
    

admin.site.register(Subdivision, SubdivisionAdmin)