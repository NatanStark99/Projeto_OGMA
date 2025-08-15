from django import template

register = template.Library()


@register.filter(name='get_field')
def get_field(form, field_name):
    return form[field_name]


@register.filter(name='get_field_label')
def get_field_label(form, field_name):
    return form[field_name].label
