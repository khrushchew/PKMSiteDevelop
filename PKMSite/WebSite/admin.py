from django.contrib import admin
from django.contrib.auth.models import User, Group

from .admins.FieldAdmin import FieldAdmin



admin.site.unregister(User)
admin.site.unregister(Group)
