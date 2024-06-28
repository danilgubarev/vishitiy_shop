from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.conf import settings

def design_page(request):
    if request.method == 'POST':
        base_structure = request.POST.get('base_structure')
        color = request.POST.get('color')
        print_or_embroidery = request.POST.get('print_or_embroidery')
        comment = request.POST.get('comment')
        design_image = request.FILES.get('design_image')

        # Формируем сообщение
        message = f"""
        Базова структура: {base_structure}
        Колір: {color}
        Прінт або вишивка: {print_or_embroidery}
        Коментар: {comment}
        """

        email = EmailMessage(
            'Дизайн від користвача',
            message,
            settings.EMAIL_HOST_USER,
            ['danilgubarev9804@gmail.com']
        )

        if design_image:
            email.attach(design_image.name, design_image.read(), design_image.content_type)
        
        email.send()

    return render(request, 'your_design/design.html')