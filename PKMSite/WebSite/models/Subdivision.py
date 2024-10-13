from django.db import models


class Subdivision(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    area = models.ForeignKey('Area', models.CASCADE, null=False, blank=False)


    class Meta:
        db_table='Subdivision'

    
    def __str__(self):
        return f"{self.name}"