from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from payments.novaposhta import NovaPoshta
from cart.cart import Cart
from . import forms


def email_form(request):
    if request.method == "POST":
        form = forms.PaymentForm(
            request.POST
        )  # Создаем форму PaymentForm из POST-запроса
        if form.is_valid():  # Проверяем валидность формы
            cd = form.cleaned_data  # Получаем очищенные данные из формы
            cart = Cart(request)  # Создаем объект корзины
            context = {
                "data": cd,
                "cart": cart,
                "user": request.user,
            }  # Формируем контекст для шаблона

            # Генерируем HTML-контент на основе шаблона 'payments/order_info.html' и контекста
            html_content = render_to_string("payments/order_info.html", context)
            plain_message = strip_tags(
                html_content
            )  # Создаем обычное текстовое сообщение без HTML-тегов

            # Выводим содержимое html_content и plain_message в консоль для отладки
            print(html_content, plain_message, sep="\n")

            # Отправляем письмо
            send_mail(
                "YOUR ORDER",  # Название сообщения
                plain_message,  # Текст сообщения без HTML
                settings.EMAIL_HOST_USER,  # кто будет отправлять
                [cd["email"]],  # получатель сообщения
                fail_silently=False,
                html_message=html_content,  # ХТМЛ содержимое письма
            )

    form = forms.PaymentForm()  # Если метод запроса GET создаем пустую форму PaymentForm
    return render(
        request, "payments/email_form.html", {"form": form},
    )  # Выводим форму на страницу email_form.html


def get_post_offices_view(request):
    np = NovaPoshta()
    print(request.GET)
    city_ref = request.GET.get("city")
    if city_ref:
        post_offices = np.get_post_offices(CityRef=city_ref)["data"]
    return render(request, "payments/partials/post_offices.html", {"post_offices": post_offices})
