from typing import Any
import json
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from . import forms

class CartMixin(FormMixin, generic.View):
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        form.process_request(request)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form: Any) -> HttpResponse:
       saved_data = form.save()
       return JsonResponse(saved_data)
    def form_invalid(self, form: Any) -> HttpResponse:
        return JsonResponse({'msg': 'Invalid data', 'errors': form.errors}, status=422)

class CartAddView(CartMixin):
    form_class = forms.CartAddForm
    
class CartUpdateView(CartMixin):
    form_class = forms.CartUpdateForm
    