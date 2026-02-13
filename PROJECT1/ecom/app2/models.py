from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    email = models.EmailField(unique=True)
