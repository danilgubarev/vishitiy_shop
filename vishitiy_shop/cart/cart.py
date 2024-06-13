from django.conf import settings


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart
        
    def add(self, **data):
        product_id = data.pop('product_id')
        if product_id not in self.cart:
            self.cart[product_id] = data
        else:
            raise ValueError('Product already in cart')
        self.save()
        return self.cart[product_id]
    
    def save(self):
        self.session.modified = True
    
    def remove(self, product_id):

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        else:
            raise ValueError('Product not in cart')
        
    def update(self, **data): 
        product_id = data.pop('product_id')
        if product_id in self.cart:
            self.cart[product_id].update(**data)
            self.save()
        else:
            raise ValueError('Product not in cart')
        return self.cart[product_id]