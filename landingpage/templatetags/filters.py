import bleach
from django import template

register = template.Library()


@register.filter_function
def format_large_number(value):
    if value >= 1000000:
        return str(value/1000000) + 'M+'
    if value >= 1000:
        return value/1000
    return value


@register.filter_function
def format_large_number_unit(value):
    if value >= 1000000:
        return 'M+'
    if value >= 1000:
        return 'K+'
    return ''


@register.filter
def sanitize_html(value):
    # Define allowed tags and attributes for sanitization
    allowed_tags = ['a', 'b', 'i', 'u', 'strong', 'em', 'p', 'br', 'ul', 'li']
    allowed_attributes = {
        '*': ['class', 'id', 'style'],
        'a': ['href', 'title']
    }
    return bleach.clean(value, tags=allowed_tags, attributes=allowed_attributes, strip=True)
