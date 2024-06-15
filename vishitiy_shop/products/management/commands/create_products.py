import random

from django.core.management.base import BaseCommand
from django.conf import settings
from faker import Faker
from products.models import Collection, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Collection.objects.create(
                name=fake.name(),
                image=fake.image_url(),
                description=fake.text(),
            )
            Product.objects.create(
                title=fake.name(),
                color=fake.hex_color(),
                size=random.choice(Product.SIZE_CHOICES)[0],
                type=random.choice(Product.PRODUCT_TYPE_CHOICES)[0],
                image="collection_ex.png",
                description=fake.text(),
                price=fake.random_int(min=1, max=100),
                collection=random.choice(Collection.objects.all()),
            )