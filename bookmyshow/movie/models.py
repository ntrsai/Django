from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.name