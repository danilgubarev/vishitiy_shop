from django.shortcuts import render
from django.http import JsonResponse
from products.models import Collection
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.


def main_view(request):
    # временное определение коллекций пока нет модели
    collections = Collection.objects.all()
    return render(request, "main/index.html", {"collections": collections})

def get_algolia_credentials(request):
    return JsonResponse({
        "APP_ID": os.getenv("ALGOLIA_APP_ID"),
        "API_KEY": os.getenv("ALGOLIA_API_KEY")
    })