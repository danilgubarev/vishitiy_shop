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
        cart = Cart(self.request)
        return cart.add(**self.cleaned_data)
            

class CartUpdateForm(CartBaseForm):
    product_id = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1)
        
    def save(self):
        cart = Cart(self.request)
        return cart.update(**self.cleaned_data)
        
        
class CartRemoveForm(CartBaseForm):
    product_id = forms.CharField(widget=forms.HiddenInput)
    
    # def clean(self):
    #     if getattr(self, 'request', None):
    #         cart = Cart(self.request)
    #         if self.cleaned_data['product_id'] not in cart:
    #             raise forms.ValidationError('Цього продукту немає в вашiй корзині')
    #     return self.cleaned_data

    def save(self):
        cart = Cart(self.request)
        return cart.remove(**self.cleaned_data)