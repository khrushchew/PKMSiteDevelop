from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'Role'
