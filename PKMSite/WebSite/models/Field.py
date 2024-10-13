from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    company = models.ForeignKey('Company', models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'Field'