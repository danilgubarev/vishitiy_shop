from colorfield.fields import ColorField
from django.db import models
from django.urls import reverse
from main.mixins import SaveSlugMixin


class Product(SaveSlugMixin, models.Model):
    SIZE_CHOICES = tuple((size, size) for size in ("XS", "S", "M", "L", "XL", "XXL"))
    COLOR_PALETTE = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red"),
        ("#00FF00", "green"),
        ("#0000FF", "blue"),
        ("#FFFF00", "yellow"),
    ]
    PRODUCT_TYPE_CHOICES = tuple(
        (type, type)
        for type in ("shoes", "t-shirt", "sweatshirt", "pants", "jacket", "sunglasses")
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    color = ColorField(image_field="image", samples=COLOR_PALETTE)
    size = models.CharField(choices=SIZE_CHOICES, max_length=3)
    type = models.CharField(choices=PRODUCT_TYPE_CHOICES, max_length=50)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    collection = models.ForeignKey(
        "Collection", on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self) -> str:
        return self.title
    
    @property
    def image_url(self):
        return self.image.url

    @property
    def url(self):
        return self.get_absolute_url()
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs) -> None:
        return super().save(slugify_value=self.title, *args, **kwargs)


class Collection(SaveSlugMixin, models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
    # @property
    # def url(self):
    #     return self.get_absolute_url()

    # def get_absolute_url(self):
    #     return reverse("products:collection", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs) -> None:
        return super().save(slugify_value=self.name, *args, **kwargs)