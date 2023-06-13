from django.urls import path, include
from .views import ProductView, CategoryView, ProductDetailView
from orders.views import order_create

urlpatterns = [
    path('', ProductView.as_view(), name='shop'),
    path('cart/', include('cart.urls')),
    path('<slug:slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='overview'),
    path('cart/create', order_create, name='order_create'),
]
