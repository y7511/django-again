from django.db import models

# Create your models here.
# models.py

from django.db import models

class CompanyInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__ (self) -> str:
     return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self) -> str:
     return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()

    image = models. ImageField(null=True)
    price = models. FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__ (self) -> str:
     return self.product_name

class abouttable(models.Model):
    imessi=models.CharField(max_length = 30)
    ronaldo=models.TextField()
    image = models. ImageField(null=True)
class contact_admin(models.Model):
    # Define fields for your Contact model
    iname = models.CharField(max_length=100)
    iprice = models. FloatField(null=True)
    imessage = models.TextField()
    iimage = models. ImageField(null=True)