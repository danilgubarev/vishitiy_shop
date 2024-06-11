from django_filters.widgets import RangeWidget

class CustomRangeWidget(RangeWidget):
    template_name = 'products/widgets/range.html'
    