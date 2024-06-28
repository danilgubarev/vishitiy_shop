from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def aboutus(request):
    return render(request, 'aboutus_contacts/about_us.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        comment = request.POST['comment']
        
        message_body = f"""
        Ім'я: {name}
        Номер телефону: {phone_number}
        Email: {email}
        Коментар: {comment}
        """

        # Отправка письма
        send_mail(
            'Контакт користувача',  # Тема письма
            message_body,  # Тело письма
            settings.EMAIL_HOST_USER,  # Отправитель
            ['danilgubarev9804@gmail.com'],  # Получатель
            fail_silently=False,
        )
    return render(request, 'aboutus_contacts/contact.html')