from django.template import Library

register = Library()


@register.filter
def text_trunc(text, size):
    return text[:size]