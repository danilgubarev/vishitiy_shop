from django.conf import settings
from products.models import Product
from decimal import Decimal

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart
        
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
            
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def contains_deep(self, product_id, **params):
        """
            Check if product in cart with all identical params 
            params: size=L, color=red, etc
        """
        if params:
            for key, value in params.items():
                if self.cart[product_id][key] != value:
                    return False
        return True
        
    def __contains__(self, product_id, **params):
        return str(product_id) in self.cart
        
    def add(self, **data) -> dict | None:
        product_id = data.pop('product_id')
        if product_id not in self.cart:
            self.save()
            self.cart[product_id] = data
            return self.cart[product_id]
    
    def save(self):
        self.session.modified = True
    
    def remove(self, product_id):
        del self.cart[product_id]
        self.save()
        return None
    
    def update(self, **data): 
        product_id = data.pop('product_id')
        if product_id in self.cart:
            self.cart[product_id].update(**data)
            self.save()
            return self.cart[product_id]
        
        
    def clear(self):
        del self.session[settings.CART_SESSION_KEY]
        self.save()