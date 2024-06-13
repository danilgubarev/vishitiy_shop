import django_filters
import django_filters.widgets
from django import forms
from .widgets import CustomRangeWidget

from .models import Product, Collection


class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(widget=CustomRangeWidget(attrs={'class': 'px-3 py-2 border border-gray-200 rounded w-24 text-center'}))
    size = django_filters.TypedMultipleChoiceFilter(
        field_name="available_sizes",
        choices=Product.SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        lookup_expr = 'icontains'
    )
    collection = django_filters.ModelMultipleChoiceFilter(
        queryset=Collection.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    color = django_filters.TypedMultipleChoiceFilter(
        field_name='available_colors',
        choices=Product.COLOR_PALETTE,
        widget=forms.CheckboxSelectMultiple,
        lookup_expr = 'icontains'
    )


    class Meta:
        model = Product
        fields = ["price", "type","size", "color", "collection"]
