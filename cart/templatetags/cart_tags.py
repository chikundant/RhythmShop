from django import template

from cart.cart import Cart

register = template.Library()


@register.simple_tag()
def get_products_count(request):
    return len(Cart(request).cart)
