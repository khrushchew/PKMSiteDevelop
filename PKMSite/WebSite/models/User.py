from django.db import models


class User(models.Model):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    subdivision = models.ForeignKey('Subdivision', models.SET_NULL, blank=True, null=True)
    role = models.ForeignKey('Role', models.SET_NULL, blank=True, null=True)
    is_activated = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=False, null=False)

    class Meta:
        db_table = 'User'

    
    def __str__(self):
        return f"{self.login}"