from cart.views import cart_add, cart_remove, cart_detail, increase_product_quantity, reduce_product_quantity
from django.urls import path

urlpatterns = [
    path('', cart_detail, name='cart'),
    path('add/<product_id>', cart_add, name='cart_add'),
    path('remove/<product_id>', cart_remove, name='cart_remove'),
    path('increase/<product_id>', increase_product_quantity, name='increase'),
    path('reduce/<product_id>', reduce_product_quantity, name='reduce')
]
