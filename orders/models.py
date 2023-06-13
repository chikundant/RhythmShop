from django.db import models
from shop.models import ProductModel
from users.models import User


class OrderModel(models.Model):
    first_name = models.CharField("Ім'я", max_length=50)
    last_name = models.CharField("Прізвище", max_length=50)
    email = models.EmailField("Пошта")
    city = models.CharField("Місто", max_length=100)
    address = models.CharField("Адреса", max_length=250)
    postal_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Усі замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return 'Order {}'.format(self.pk)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.pk)

    def get_cost(self):
        return self.price * self.quantity
