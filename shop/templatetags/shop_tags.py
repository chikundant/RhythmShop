from django import template

from shop.models import CategoryModel

register = template.Library()


@register.simple_tag()
def get_categories():
    return CategoryModel.objects.filter(parent_category=None).prefetch_related('children')
