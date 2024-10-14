from django.contrib import admin
from ..models.User import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'password', 'subdivision', 'role', 'is_activated', 'profile_picture')
    ordering = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(subdivision__area__department__field__company__code=request.user.username)
    

admin.site.register(User, UserAdmin)