from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from payments.novaposhta import NovaPoshta
from cart.cart import Cart
from . import forms
from django.views import View
import requests
from django.http import JsonResponse, HttpResponse

import uuid
import json

token_api = 'ueWjGTgQC_DzAcbRzquc8THn_H1TwNbyeLZZ2AAsdIKs'
merchant_invoice_id = str(uuid.uuid4())

def email_form(request):
    if request.method == "POST":
        print('got post req in email form view')
        form = forms.PaymentForm(
            request.POST
        )  # Создаем форму PaymentForm из POST-запроса
        if form.is_valid():  # Проверяем валидность формы
            cd = form.cleaned_data  # Получаем очищенные данные из формы
            cd['post_office'] = NovaPoshta().get_post_offices(Ref=cd['post_office'])["data"][0]["Description"]
            cd['city'] = NovaPoshta().get_cities(Ref=cd['city'])["data"][0]["Description"]
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
            print("BEFORE SENDING REQUEST")
            # Отправляем письмо
            send_mail(
                "YOUR ORDER",  # Название сообщения
                plain_message,  # Текст сообщения без HTML
                settings.EMAIL_HOST_USER,  # кто будет отправлять
                [cd["email"]],  # получатель сообщения
                fail_silently=False,
                html_message=html_content,  # ХТМЛ содержимое письма
            )
            return redirect("payments:monobank-payment")
        else:
            return render(request, "payments/email_form.html", {"form": form})

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



def monobank_form_view(request):
    token = 'uxU1BEAybhI6zQy1GLD_oK0wLU1rvU8o1ry5VLfA5c84'
   
    if request.method == "POST":
        print('got post req')
        form = forms.MonobankPaymentForm(
            request.POST
        )  # Создаем форму PaymentForm из POST-запроса
        if form.is_valid():  # Проверяем валидность формы
            print('form is valid')
            cd = form.cleaned_data  # Получаем очищенные данные из формы
            cart = Cart(request)  # Создаем объект корзины
            basket_order = []
            for item in cart:
                basket_order.append({
                    "name": item["product"].title,
                    "qty": item["quantity"],
                    "sum": int(item["total_price"]),
                    "icon": item["product"].image.url,
                    "unit": "шт.",
                    "code": item["product"].slug,
                    "barcode": "string",
                    "header": "string",
                    "footer": "string",
                    "tax": [ ],
                })
            data = {
                "amount": int(cart.get_total() * 100),
                "cardData": cd,
                "merchantPaymInfo": {
                    "reference": str(uuid.uuid4()),
                    "destination": "Оплата замовлення",
                    "basketOrder": basket_order
                },
                "redirectUrl": request.build_absolute_uri(reverse('payments:payment-status')),
                "webhookUrl": request.build_absolute_uri(reverse('payments:webhook')),
                "initiationKind": "client",
            }

            headers = {
                'X-token':token,
                'Content-Type': 'application/json'
            }
            resp = requests.post(
                "https://api.monobank.ua/api/merchant/invoice/payment-direct",
                json=data,
                headers=headers
            )
            print(resp.status_code, resp.json())
            if resp.status_code == 200:
                data = resp.json()
                confirm_url = data.get('tdsUrl')
                if confirm_url:
                    return redirect(confirm_url)
            return redirect(data.get('redirectUrl'))

    form = forms.MonobankPaymentForm()
    return render(request, "payments/monobank_payment_form.html", {"form": form})
    
    
def monobank_webhook_view(request):
    payload = json.loads(request.body)
    print('WEBHOOK PAYLOAD: ', payload)
    if payload.get("status") == "success":
        return HttpResponse(status=200)
    
def payment_status_view(request):
    print('paymetns status')
    return HttpResponse()