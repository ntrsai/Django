from django.db import models

# Create your models here.
class bookstore(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=100)




