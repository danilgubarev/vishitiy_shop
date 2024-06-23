from django.contrib import admin
from django import forms

from .models import Collection, Product

# Register your models here.
admin.site.register(Collection)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Модель для админки
    Указания отображаемых полей и переопределение метода получения формы для замены виджета.
    """

    list_display = ["title", "final_price", "collection", "available"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["available_sizes"].widget = forms.CheckboxSelectMultiple(
            choices=Product.SIZE_CHOICES,
            attrs={"class": "form-control"},
        )
        form.base_fields["available_colors"].widget = forms.CheckboxSelectMultiple(
            choices=Product.COLOR_PALETTE, attrs={"class": "form-control"}
        )
        return form
