from django.shortcuts import render

# Create your views here.


def email_form(request):
    return render(request, 'payments/email_form.html')