from django.contrib import admin
from .models import Collections, Product

# Register your models here.
admin.site.register((Collections, Product))