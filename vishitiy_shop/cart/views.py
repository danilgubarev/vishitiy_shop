from typing import Any
from django.views import generic
from django.views.generic.edit import FormMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from . import forms

class CartMixin(FormMixin, generic.View):
    status_code = 200
    msg = None
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        form.process_request(request)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form: Any) -> HttpResponse:
       saved_data = form.save() or {}
       return JsonResponse({'data': saved_data, 'msg': self.msg}, status=self.status_code)
    
    def form_invalid(self, form: Any) -> HttpResponse:
        return JsonResponse({'msg': 'Ошибка валидации', 'errors': form.errors}, status=422)

class CartAddView(CartMixin):
    form_class = forms.CartAddForm
    msg = 'Товар додано до кошика'
    
class CartUpdateView(CartMixin):
    form_class = forms.CartUpdateForm
    msg = 'Кількість змінено'
    
class CartRemoveView(CartMixin):
    form_class = forms.CartRemoveForm
    status_code = 204