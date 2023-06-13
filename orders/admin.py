from django.contrib import admin
from .models import OrderModel, OrderItemModel


class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(OrderModel, OrderAdmin)
