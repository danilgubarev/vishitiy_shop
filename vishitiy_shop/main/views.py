from django.shortcuts import render
from products.models import Collection

# Create your views here.


def main_view(request):
    # временное определение коллекций пока нет модели
    collections = Collection.objects.all()
    return render(request, "main/index.html", {"collections": collections})
