from django import template
from django.utils.safestring import mark_safe

#register的名字是固定的，不可改变
register = template.Library()


@register.filter
def filter_multi(x,y):
    return x*y


@register.simple_tag
def simple_tag_multi(x,y,z):
    return x*y*z