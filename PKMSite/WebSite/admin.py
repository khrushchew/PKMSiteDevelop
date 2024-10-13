from django.contrib import admin
from django.contrib.auth.models import User, Group

from .admins.FieldAdmin import FieldAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


admin.site.site_header="Управление базой данных компании"
admin.site.index_title="Ваши таблицы:"