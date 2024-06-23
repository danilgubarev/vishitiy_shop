from django.shortcuts import render
from django.http import JsonResponse
from itertools import zip_longest
from products.models import Collection, Product
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.


def main_view(request):
    """
    Отображение главной страницы с коллекциями и продуктами со скидкой больше 30%.
    Продукты группируются в группы по 4 для отображения в карусели
    (возвращаеться список итераторов по 4 элемента в каждом).
    """
    discounted_products = Product.objects.filter(discount__gte=20)
    context = {
        "collections": Collection.objects.all(),
        "discounted_products_grouped": zip_longest(
            *[iter(discounted_products)] * 4, fillvalue=None
        ),
    }
    return render(request, "main/index.html", context)


def get_algolia_credentials(request):
    return JsonResponse(
        {"APP_ID": os.getenv("ALGOLIA_APP_ID"), "API_KEY": os.getenv("ALGOLIA_API_KEY")}
    )
