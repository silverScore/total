import logging
from django import template
from urllib.parse import urlencode
from django.template.defaultfilters import stringfilter

register = template.Library()

# ex) <a href="{% url 'videos:index'}{% urlparams page='1' tag='sometag' %}">Next</a>
@register.simple_tag
def urlparams(*_, **kwargs):
    safe_args = {k: v for k, v in kwargs.items() if v is not None}
    if safe_args:
        return '?{}'.format(urlencode(safe_args))
    return ''


@register.filter
def sub(value, arg):
    return value - arg
