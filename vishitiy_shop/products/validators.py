from django.forms import ValidationError


class ProductSizeValidator:
    def __init__(self, acceptable_sizes: list) -> None:
        # приведение к одному регистру
        for index, size in enumerate(acceptable_sizes):
            acceptable_sizes[index] = size.upper()
        self.ACCEPTABLE_SIZES = acceptable_sizes           
    def check_size(self, value: str) -> None:
        if value not in self.ACCEPTABLE_SIZES:
            raise ValidationError(f"{value} is not an available size")
    def validate_size(self, values: str | list) -> None:
        # if values is sigle str object
        if isinstance(values, str):
            return self.check_size(values)
        # if values is list
        for value in values:
            value = value.upper()
            return self.check_size(value)