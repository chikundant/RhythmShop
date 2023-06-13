from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch


from .forms import UserLoginForm, UserRegisterForm
from orders.models import OrderModel, OrderItemModel


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class MyOrdersView(LoginRequiredMixin, ListView):
    template_name = 'users/my_orders.html'
    context_object_name = 'orders'
    model = OrderModel

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        queryset = queryset.prefetch_related(Prefetch('items', queryset=OrderItemModel.objects.select_related('product')))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = context['orders']
        order_items = []
        for order in orders:
            order_items.extend(order.items.all())
        context['order_items'] = order_items
        return context


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('profile')


class RegistrationView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')


class UserLogoutView(LogoutView):
    next_page = 'home'

