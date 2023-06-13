from django.core.mail import send_mail
from .models import OrderModel, OrderItemModel, User
from rhythm import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rhythm.celery import celery


@celery.task
def send_email(order_id):
    order = OrderModel.objects.get(pk=order_id)
    items = OrderItemModel.objects.filter(order=order)
    subject = 'Замовлення номер {}'.format(order_id)
    html_message = render_to_string('orders/email.html', {'order': order, 'items': items})
    message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [order.email, ]

    send_mail(subject, message, email_from, recipient_list, fail_silently=False)


@celery.task
def send_beat_email():
    subject = 'Spam'
    # html_message = render_to_string('orders/email.html', {'order': order, 'items': items})
    html_message = 'Message'
    message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    for user in User.object.all():
        send_mail(subject, message, email_from, user.email, fail_silently=False)
