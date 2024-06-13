from typing import Any
import json
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from . import forms

# Create your views here.
class CartAddView(generic.FormView):
    form_class = forms.CartAddForm
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
def cart_add_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = forms.CartAddForm(data)
        form.process_request(request)
        if form.is_valid():
            saved_data = form.save()
            if saved_data:
                return JsonResponse(saved_data)
        return JsonResponse({'msg': 'Invalid data', 'errors': form.errors}, status=400)