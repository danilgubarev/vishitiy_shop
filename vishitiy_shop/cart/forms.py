from .cart import Cart
from django import forms 
from products.validators import ProductSizeValidator
from products.models import Product

class CartBaseForm(forms.Form):
    def process_request(self, request):
        print("CALLING METHOD", request)
        self.request = request

    def save(self):
        assert self.is_valid(), 'Form is not valid'
        assert self.request, 'Request is not provided'

class CartAddForm(CartBaseForm):
    product_id = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(initial=1, min_value=1, required=False)
    size = forms.CharField(validators=[ProductSizeValidator(Product.ACCEPTABLE_SIZES).validate_size])
    color = forms.CharField()
    price = forms.DecimalField()
    
    def clean(self):
        if getattr(self, 'request', None):
            cart = Cart(self.request)
            if self.cleaned_data['product_id'] in cart:
                raise forms.ValidationError('Продукт вже знаходиться в корзині')
        return self.cleaned_data

    def save(self):
        super().save()
        self.cleaned_data['price'] = str(self.cleaned_data['price'])
        if self.request:
            cart = Cart(self.request)
            return cart.add(**self.cleaned_data)
            

class CartUpdateForm(CartAddForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['final_price']
        for field in self.fields.values():
            field.required = False
        self.fields['product_id'].required = True
        
    def save(self):
        if self.request:
            cart = Cart(self.request)
            return cart.update(**self.cleaned_data)