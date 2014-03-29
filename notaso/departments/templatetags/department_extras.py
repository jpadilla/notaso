from django import template
register = template.Library()


@register.filter(name='count_professors')
def count_professors(instance, university):
    return instance.count(university)
