from .cart import Cart
from django import forms 
from products.validators import ProductSizeValidator
from products.models import Product

class CartAddForm(forms.Form):
    product_id = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(initial=1, min_value=1, required=False)
    size = forms.CharField(validators=[ProductSizeValidator(Product.ACCEPTABLE_SIZES).validate_size])
    color = forms.CharField()
    price = forms.DecimalField()
    
    def process_request(self, request):
        self.request = request

    def save(self):
        print(self.is_valid())
        assert self.is_valid(), 'Form is not valid'
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
        self.request = kwargs.pop('request', None)
        
    def save(self):
        if self.request:
            cart = Cart(self.request)
            return cart.update(**self.cleaned_data)