from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Customer_Detail(models.Model):
    Customer_Detail = models.OneToOneField(Customer,on_delete=models.CASCADE)
    c_id = models.IntegerField
    city = models.CharField(max_length=20)
    Nationality = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.city

class Product(models.Model):
    Product = models.ManyToManyField(Customer)
    p_name = models.CharField(max_length=40)
    quantity = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return self.p_name
    

class Categeories(models.Model):
    name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='products/', null=True,blank=True)

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    Categeories = models.ForeignKey(Categeories,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Image = models.ImageField(upload_to='products/', null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.name
    

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username