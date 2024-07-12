from django.db import models

# Create your models here.
class Bat(models.Model):
    name=models.CharField(max_length=50)
    runs=models.FloatField()
    team=models.CharField(max_length=50)

