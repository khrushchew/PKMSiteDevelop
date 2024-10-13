from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    field = models.ForeignKey('Field', models.CASCADE, blank=False, null=False)
    indent = models.IntegerField(default=0, blank=False, null=False)
    user_id = models.ForeignKey('User', models.SET_NULL, blank=True, null=True)
    areas_quantity = models.IntegerField(default=0, blank=False, null=False)
    machines_quantity = models.IntegerField(default=0, blank=False, null=False)
    operators_quantity = models.IntegerField(default=0, blank=False, null=False)
    support_stuff_quantity = models.IntegerField(default=0, blank=False, null=False)

    class Meta:
        db_table = 'Department'