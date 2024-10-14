from django.contrib import admin
from django.contrib.auth.models import User, Group

from .admins.FieldAdmin import FieldAdmin
from .admins.DepartmentAdmin import DepartmentAdmin
from .admins.RoleAdmin import RoleAdmin
from .admins.AreaAdmin import AreaAdmin
from .admins.SubdivisionAdmin import SubdivisionAdmin
from .admins.UserAdmin import UserAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


admin.site.site_header="Управление базой данных компании"
admin.site.index_title="Ваши таблицы:"