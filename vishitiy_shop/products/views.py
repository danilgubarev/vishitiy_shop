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
        filterset = ProductFilter(self.request.GET, queryset=qs)
        # print(f"NEW QUERYSET FOR PARAMS {self.request.GET} IS {filterset.qs}")
        # print(filterset.qs[0].size, filterset.qs[0].price)
        # return filterset.qs


def product_page(request):
    return render(request, 'products/product_list.html')