from django.shortcuts import render

# Create your views here.


def main_view(request):
    # временное определение коллекций пока нет модели
    collections = [
        "nike",
        "Jujutsu kaisen",
        "GYM",
        "couples",
        "JDM & CARS",
        "money",
        "art",
        "country",
    ]
    return render(request, "main/index.html", {"collections": collections})
