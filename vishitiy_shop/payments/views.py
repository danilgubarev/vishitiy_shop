from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from cart.cart import Cart
from . import forms

email_of_provider = ''

def email_form(request):
    if request.method == 'POST':
        form = forms.PaymentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart = Cart(request)
            context = {'person_data': cd, 'cart': cart, 'user': request.user}
            html_content = render_to_string('payments/order_info.html', context)
            plain_message = strip_tags(html_content)
            
            print(html_content, plain_message, sep="\n")

            send_mail(
                'YOUR ORDER',
                plain_message,
                settings.EMAIL_HOST_USER,
                [cd["email"]],
                fail_silently=False,
                html_message=html_content
            )

        return HttpResponse("Email sent successfully")
    form = forms.PaymentForm()
    return render(request, 'payments/email_form.html', {'form': form})