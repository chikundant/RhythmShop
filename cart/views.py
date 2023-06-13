from django.shortcuts import render, redirect, get_object_or_404
from shop.models import ProductModel
from .cart import Cart
from orders.forms import OrderCreateForm


def cart_detail(request):
    cart = Cart(request)

    context = \
        {
            'cart': cart,
            'form': OrderCreateForm()

        }
    return render(request, 'cart/cart_detail.html', context=context)


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductModel, id=product_id)

    cart.add(product=product)
    return redirect('cart')


def increase_product_quantity(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductModel, id=product_id)
    cart.increase_product_quantity(product)
    return redirect('cart')


def reduce_product_quantity(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductModel, id=product_id)
    cart.reduce_quantity(product)
    return redirect('cart')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductModel, id=product_id)
    cart.remove(product)
    return redirect('cart')
