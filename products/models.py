from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(blank=True)
    category = models.IntegerField()
