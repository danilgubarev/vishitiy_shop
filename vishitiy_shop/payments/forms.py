from django import forms
from django_countries import countries
from django_countries.fields import CountryField

class PaymentForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефону')
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Ім`я')
    country = CountryField().formfield(label="Країна")
    city = forms.CharField(label='Місто')
    post = forms.CharField(label='Поштова адреса')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'border border-light text-white bg-black'})
    
    
# number = request.POST.get('number')
#         email = request.POST.get('email')
#         name = request.POST.get('name')
#         country = request.POST.get('country')
#         city = request.POST.get('city')
#         post = request.POST.get('post')