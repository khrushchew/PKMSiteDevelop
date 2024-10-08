from django.contrib import admin
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


# from . import models, nzt_models

# class CustomAdminSite(admin.AdminSite):
#     def get_model_perms(self, request, obj=None):
#         """
#         Определяем, какие модели отображать в зависимости от логина пользователя.
#         """
#         if request.user.username == 'pkm':
#             return {
#                 'PKMOrder': True,
#             }
#         elif request.user.username == 'ntz':
#             return {
#                 'NTZUser': True,
#             }
#         return {}

# custom_admin_site = CustomAdminSite(name='custom_admin')

# # Регистрируем модели для PKM
# custom_admin_site.register(models.PKMOrder)

# # Регистрируем модели для NTZ
# custom_admin_site.register(nzt_models.NTZUser)

