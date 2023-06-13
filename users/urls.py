from django.urls import path
from .views import ProfileView, UserLoginView, UserLogoutView, RegistrationView, MyOrdersView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('my_orders/', MyOrdersView.as_view(), name='my_orders'),
]
