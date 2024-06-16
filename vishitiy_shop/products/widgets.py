from django_filters.widgets import RangeWidget
from django import forms

class CustomRangeWidget(RangeWidget):
    template_name = 'products/widgets/range.html'
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs'] = {'min': self.attrs.get('min', 0), 'max': self.attrs.get('max', 5000)}
        for subcontext, suffix in zip(context["widget"]["subwidgets"], self.suffixes):
            #x-on:input="mintrigger"
            #x-model="minprice"
            # subcontext["attrs"][suffix+"length"] = len(str(context['widget']['attrs'][suffix]))
            subcontext["attrs"]["x-on:input"] = suffix + "trigger"
            subcontext["attrs"]["x-model"] = suffix + "price"
        return context

    