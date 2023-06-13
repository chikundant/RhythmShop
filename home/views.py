from django.views.generic import ListView

from shop.models import CategoryModel


class Home(ListView):
    model = CategoryModel
    template_name = 'home/index.html'
    context_object_name = 'category'

