from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from cart.cart import Cart
import requests
import json
import time
import hashlib
from django.views.decorators.csrf import csrf_exempt
from . import forms


email_of_provider = ''

def email_form(request):
    api_url = 'https://api.novaposhta.ua/v2.0/json/'
    api_key = 'd163f31ac2f2738242a3c3d2875c8020'

    # Получение списка городов
    cities_response = requests.post(api_url, json={
        'apiKey': api_key,
        'modelName': 'Address',
        'calledMethod': 'getCities',
        'methodProperties': {}
    })
    cities_data = cities_response.json()['data']

    if request.method == 'POST':
        form = forms.PaymentForm(request.POST)  # Создаем форму PaymentForm из POST-запроса
        if form.is_valid():  # Проверяем валидность формы
            cd = form.cleaned_data  # Получаем очищенные данные из формы
            cart = Cart(request)  # Создаем объект корзины
            context = {'data': cd, 'cart': cart, 'user': request.user}  # Формируем контекст для шаблона

            # Генерируем HTML-контент на основе шаблона 'payments/order_info.html' и контекста
            html_content = render_to_string('payments/order_info.html', context)
            plain_message = strip_tags(html_content)  # Создаем обычное текстовое сообщение без HTML-тегов
            
            # Выводим содержимое html_content и plain_message в консоль для отладки
            print(html_content, plain_message, sep="\n")

            # Отправляем письмо
            send_mail(
                'YOUR ORDER',  # Название сообщения
                plain_message,  # Текст сообщения без HTML
                settings.EMAIL_HOST_USER,  # кто будет отправлять
                [cd["email"]],  # получатель сообщения
                fail_silently=False,  
                html_message=html_content  # ХТМЛ содержимое письма
            )
    elif request.method == 'GET' and 'city_id' in request.GET:
        
        city_id = request.GET['city_id']
        post_offices_response = requests.post(api_url, json={
            'apiKey': api_key,
            'modelName': 'AddressGeneral',
            'calledMethod': 'getWarehouses',
            'methodProperties': {'CityRef': city_id}
        })
        post_offices_data = post_offices_response.json()['data']
        return JsonResponse({'post_offices': post_offices_data})
    
    
    first_city_id = cities_data[0]['Ref']
    post_offices_data = []

    if first_city_id:
        post_offices_response = requests.post(api_url, json={
            'apiKey': api_key,
            'modelName': 'AddressGeneral',
            'calledMethod': 'getWarehouses',
            'methodProperties': {'CityRef': first_city_id}
        })
        post_offices_data = post_offices_response.json()['data']

    form = forms.PaymentForm()  # Если метод запроса GET создаем пустую форму PaymentForm
    return render(request, 'payments/email_form.html', {'form': form, 'cities': cities_data,
            'post_offices': post_offices_data,})  # Выводим форму на страницу email_form.html
