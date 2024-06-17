from cart.cart import Cart

def cart(request):
    """Создания контекстного процессора, что бы корзина была доступна в контексе каждого шаблона"""
    return {'cart': Cart(request)}