from django.db import models

# Create your models here.
class Ball(models.Model):
    name=models.CharField(max_length=50)
    wickets=models.FloatField()
    team=models.CharField(max_length=50)
