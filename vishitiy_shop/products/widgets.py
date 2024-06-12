from django_filters.widgets import RangeWidget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class CustomRangeWidget(RangeWidget):
    template_name = 'products/widgets/range.html'
    def __init__(self, attrs=None):
        self.attrs = attrs
        super().__init__(attrs)
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs'] = {'min': self.attrs.get('min', 0), 'max': self.attrs.get('max', 1000)}
        for subcontext, suffix in zip(context["widget"]["subwidgets"], self.suffixes):
            #x-on:input="mintrigger"
            #x-model="minprice"
            subcontext["attrs"]["x-on:input"] = suffix + "trigger"
            subcontext["attrs"]["x-model"] = suffix + "price"
        return context

    