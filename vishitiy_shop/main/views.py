from django.shortcuts import render
from products.models import Collections

# Create your views here.


def main_view(request):
    # временное определение коллекций пока нет модели
    collections = Collections.objects.all()
    return render(request, "main/index.html", {"collections": collections})
