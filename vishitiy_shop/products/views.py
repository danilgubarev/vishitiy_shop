from typing import Any
from django.shortcuts import render
from django.views import generic
from . models import Product
from django.db.models import QuerySet
from .filters import ProductFilter

# Create your views here.
class ProductListView(generic.ListView):
    template_name = 'products/product_list.html'
    queryset = Product.objects.all().select_related("collection")
    
    def get_queryset(self) -> QuerySet[Product]:
        qs = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=qs)
        print("REd products", Product.objects.filter(color="#ff0000"))
        return self.filterset.qs
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context
