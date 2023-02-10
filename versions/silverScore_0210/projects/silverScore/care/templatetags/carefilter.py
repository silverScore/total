# 해당 caretfilter.py 는 config/settings.py 의 Templates 에 추가하여 커스텀 템플릿 태그같은 공통모듈을 사용하도록 함.
# ref : https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/
import logging
from django import template

from urllib.parse import urlencode
from django.template.defaultfilters import stringfilter

register = template.Library()

# @register.simple_tag
# def filter_element(value):
#    if value:
#        return f'{value}'


# @register.simple_tag
# def test_tag():
#    return 'test tag'


# ex) <a href="{% url 'videos:index'}{% urlparams page='1' tag='sometag' %}">Next</a>
@register.simple_tag
def urlparams(*_, **kwargs):
    safe_args = {k: v for k, v in kwargs.items() if v is not None}
    if safe_args:
        return '?{}'.format(urlencode(safe_args))
    return ''
