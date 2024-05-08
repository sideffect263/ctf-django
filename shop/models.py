from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
    def __str__(self):
        return self.title+" "+str(self.price)
    
    
    
class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    city=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    total = models.FloatField(default=1)
    def __str__(self):
        return self.name

    