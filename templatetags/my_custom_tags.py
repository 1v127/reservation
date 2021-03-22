from django import template

register=template.librry()

@register.simple_tag
def my_tag(arg):
    return arg