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
    city = forms.CharField(
        label="Назва або Індекс населеного пункту"
    )
    post_office = forms.CharField(
        label="Відділення Нової пошти",
        widget=forms.Select(),
    )

    # конструктор класса PaymentForm
    def __init__(self, *args, **kwargs):
        # Вызывает конструктор родительского класса (forms.Form).
        super().__init__(*args, **kwargs)
        # проходится (переьирает) все поля формы
        self.fields["city"].widget.attrs.update(
            {
                "hx-get": reverse("payments:get-cities"),
                "hx-trigger": "input changed delay:500ms, search",
                "hx-target": "#div_id_city",
                "hx-swap": "beforeend"
            }
        )
        self.fields["post_office"].widget.attrs.update(
            {
                "hx-get": reverse("payments:get-post-offices"),
                "hx-trigger": "input changed delay:500ms, search",
                "hx-target": "#div_id_post_office",
                "hx-include": "#div_id_city input",
            }
        )
        for field in self.fields:
            # Обновляет атрибуты виджета каждого поля формы
            self.fields[field].widget.attrs.update(
                {"class": "border border-light text-white bg-black"}
            )
            
    def clean_post_office(self):
        post_office_id = self.cleaned_data["post_office"]
        post_office = np.get_post_offices(Ref=post_office_id)["data"]
        if not post_office_id:
            raise forms.ValidationError("Виберіть відділення Нової пошти")
        elif post_office == []:
            raise forms.ValidationError("Такого відділення Нової пошти не існує")
        return post_office_id
    
class MonobankPaymentForm(forms.Form):
    pan = forms.CharField(max_length=16, min_length=16, label="Номер картки")
    cvv = forms.CharField(max_length=3, min_length=3, label="CVV")
    exp = forms.CharField(max_length=4,
        min_length=4,
        label="Кінцевий термін",
        help_text="MMYY"
    )