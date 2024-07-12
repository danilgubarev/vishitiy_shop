# Generated by Django 5.0.6 on 2024-06-13 12:49

import django.core.validators
import products.models
from django.db import migrations, models

import products.validators


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='available_sizes',
            field=models.JSONField(default=list, validators=[products.validators.ProductSizeValidator(products.models.Product.ACCEPTABLE_SIZES).validate_size]),
        ),
    ]