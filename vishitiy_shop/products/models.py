from django.db import models
from colorfield.fields import ColorField

class Product(models.Model):
    SIZE_CHOICES = tuple((size, size) for size in ('XS', 'S', 'M', 'L', 'XL', 'XXL'))
    COLOR_PALETTE = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red"),
        ("#00FF00", "green"),
        ("#0000FF", "blue"),
        ("#FFFF00", "yellow"),
    ]
    title = models.CharField(max_length=150)
    color = ColorField(image_field="image", samples=COLOR_PALETTE)
    size = models.CharField(choices=SIZE_CHOICES, max_length=3)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    collection = models.ForeignKey("Collections", on_delete=models.CASCADE, related_name='products')
    
    def __str__(self) -> str:
        return self.title
    

class Collections(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title