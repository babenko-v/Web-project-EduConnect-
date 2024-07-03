
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='default_no_info')
def default_no_info(value):
    if value != "None" and value:
        if isinstance(value, int) and value < 100:
            return f"{value} years"
        return value
    else:
        return mark_safe("<i>Information not provided</i>")

