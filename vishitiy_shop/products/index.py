from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    """Индекс содержащий поля продуктов, значение которых попадут в индекс"""
    fields = ('title', 'type', 'url', 'image_url', 'price')
    index_name = 'products'
    settings = {
        'searchableAttributes': ['title'],
        'attributesForFaceting': ['color', 'size', 'type']
    }
