
from django import template 


register = template.Library()


@register.filter(name='capital_letter')
def capital_letter(value):
    return value.upper()

@register.filter(name='base_price')
def get_base_price(value):
    value * 10