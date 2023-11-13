from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    image = models.CharField(max_length=2083)

class ProductAll(models.Model):
     name=models.CharField(max_length=255)
     product = models.ManyToManyField(Product, related_name='products')