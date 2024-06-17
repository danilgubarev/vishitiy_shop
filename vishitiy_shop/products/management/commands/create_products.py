import random

from django.core.management.base import BaseCommand
from django.conf import settings
from faker import Faker
from products.models import Collection, Product


class Command(BaseCommand):
    """ Management команда для наполнения базы данных.
    Используется библиотека faker для генерации случайных данных.
    Запуск: python manage.py create_products.
    """
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
                available_colors=random.sample([color[0] for color in Product.COLOR_PALETTE], 3),
                available_sizes=random.sample(Product.ACCEPTABLE_SIZES, 3),
                type=random.choice(Product.PRODUCT_TYPE_CHOICES)[0],
                discount=random.choice([0, 10, 20, 50]),
                image="collection_ex.png",
                description=fake.text(),
                price=fake.random_int(min=100, max=5000),
                collection=random.choice(Collection.objects.all()),
            )
