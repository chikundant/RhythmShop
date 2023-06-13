from django.shortcuts import render
from .models import OrderItemModel
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import send_email


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid() and cart:
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            for item in cart:
                OrderItemModel.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            send_email.delay(order.pk)
            return render(request, 'orders/success.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'cart/cart_detail.html',
                  {'cart': cart, 'form': form})
