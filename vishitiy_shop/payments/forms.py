from django import forms  # Импортируем forms из Django для создания форм
from django.urls import reverse
from django_countries.fields import (
    CountryField,
)  # Импортируем поле страны из django-countries
from .novaposhta import NovaPoshta

np = NovaPoshta()


class PaymentForm(forms.Form):
    phone_number = forms.CharField(
        label="Номер телефону"
    )  # поле для ввода номера телефона
    email = forms.EmailField(label="Email")  # поле для ввода email
    name = forms.CharField(label="Ім`я")  # поле для ввода имени
    country = CountryField().formfield(
        label="Країна"
    )  # поле для выбора страны используя библиотеку django-countries )))
    post = forms.CharField(label="Поштовий індекс")  # Поле для ввода почтового индекса
    city = forms.ChoiceField(
        label="Місто",
        choices=[
            (city["Ref"], city["Description"]) for city in np.get_cities()["data"]
        ],
    )
    post_office = forms.ChoiceField(
        label="Відділення Нової пошти",
        choices=[]
    )

    # конструктор класса PaymentForm
    def __init__(self, *args, **kwargs):
        # Вызывает конструктор родительского класса (forms.Form).
        super().__init__(*args, **kwargs)
        # проходится (переьирает) все поля формы
        self.fields["city"].widget.attrs.update(
            {
                "hx-get": reverse("payments:get-post-offices"),
                "hx-trigger": "change",
                "hx-target": "#div_id_post_office select",
            }
        )
        for field in self.fields:
            # Обновляет атрибуты виджета каждого поля формы
            self.fields[field].widget.attrs.update(
                {"class": "border border-light text-white bg-black"}
            )
