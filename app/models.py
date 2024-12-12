from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    description = models.TextField()
    categories = models.CharField(max_length=255)
