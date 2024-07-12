from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    category=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    quantity=models.IntegerField()
    is_active=models.BooleanField()
    image=models.ImageField(upload_to='image')
