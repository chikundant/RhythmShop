from django.views.generic import ListView, DetailView

from .models import CategoryModel, ProductModel
from cart.forms import CartAddProductForm
class ProductView(ListView):
    model = ProductModel
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    paginate_by = 12


class CategoryView(ListView):
    model = CategoryModel
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return ProductModel.objects.filter(category__slug=self.kwargs['slug']).prefetch_related('category')


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddProductForm()
        return context
