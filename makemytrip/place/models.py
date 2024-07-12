from django.db import models


# Create your models here.
class place(models.model):
    name = models.CharField(max_length=50)
    city_name = models.DataField()
