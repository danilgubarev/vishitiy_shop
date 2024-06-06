from django.shortcuts import render
from django.views import generic
from . models import Product
from django.db.models import QuerySet

# Create your views here.
class ProductListView(generic.ListView):
    template_name = 'products/product_list.html'
    queryset = Product.objects.all().select_related("collection")