from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=255, null=False, blank = False)
    indent = models.IntegerField(default=0, blank=False, null=False)
    department = models.ForeignKey('Department', models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'Area'
