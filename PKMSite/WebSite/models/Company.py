from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=100, null=False, blank=False)
    is_paid = models.BooleanField(default=False, blank=False)
    paid_machines_quantity = models.IntegerField(default=0, null=True, blank=True)
    date_of_start = models.DateField(null=True, blank=True)
    date_of_end = models.DateField(null=True, blank=True)
    is_testdrive = models.BooleanField(default=True)
    number_of_support_staff = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        db_table = 'Company'


    def __str__(self):
        return f"{self.name}"
