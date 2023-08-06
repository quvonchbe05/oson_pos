from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    sale_price=models.PositiveIntegerField()
    bar_code = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name