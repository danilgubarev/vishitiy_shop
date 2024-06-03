from django.shortcuts import render

# Create your views here.


def main_view(request):
    # временное определение коллекций пока нет модели
    collections = [
        "nike",
        "adidas",
        "puma",
        "new balance",
        "reebok",
        "vans",
        "jordan",
        "asics",
    ]
    return render(request, "main/index.html", {"collections": collections})
