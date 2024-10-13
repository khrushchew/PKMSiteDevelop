from django.db import models


class User(models.Model):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    company = models.ForeignKey('Company', models.CASCADE, blank=True, null=True)
    role = models.ForeignKey('Role', models.SET_NULL, blank=True, null=True)
    is_activated = models.BooleanField(default=False)

    class Meta:
        db_table = 'User'