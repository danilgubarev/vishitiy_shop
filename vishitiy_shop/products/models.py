from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from main.mixins import SaveSlugMixin
from products.validators import ProductSizeValidator

class Product(SaveSlugMixin, models.Model):
    ACCEPTABLE_SIZES = ["XS", "S", "M", "L", "XL", "XXL"]
    SIZE_CHOICES = tuple((size, size) for size in ACCEPTABLE_SIZES)
    COLOR_PALETTE = tuple((color, color) for color in ("white", "black", "red", "green", "blue", "yellow"))
    PRODUCT_TYPE_CHOICES = tuple(
        (type, type)
        for type in ("shoes", "t-shirt", "sweatshirt", "pants", "jacket", "sunglasses")
    )
    
    SIZE_VALIDATOR = ProductSizeValidator(ACCEPTABLE_SIZES)
    
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    available_colors = models.JSONField(default=list)
    available_sizes = models.JSONField(default=list, validators=[SIZE_VALIDATOR.validate_size])
    available = models.BooleanField(default=True)
    type = models.CharField(choices=PRODUCT_TYPE_CHOICES, max_length=50)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    collection = models.ForeignKey(
        "Collection", on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self) -> str:
        return self.title
    
    @property
    def image_url(self):
        return self.image.url
    
    @property
    def final_price(self):
        return self.price - (self.price * self.discount / 100)

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