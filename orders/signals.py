from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Order
from robots.models import Robot


@receiver(post_save, sender=Robot)
def check_expected_robots(sender, instance, **kwargs):
    waiting_orders = Order.objects.filter(wait=True, robot_serial=instance.serial)
    if waiting_orders.exists():
        customer_email = waiting_orders[0].customer.email
        robot_model = instance.model
        robot_version = instance.version
        send_email(robot_model, robot_version, customer_email)
        waiting_orders[0].wait = False
        waiting_orders[0].save()


def send_email(robot_model, robot_version, customer_email):
    subject = 'Робот доступен'
    message = f'Добрый день!\nНедавно вы интересовались нашим роботом модели {robot_model}, версии ' \
              f'{robot_version}.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, ' \
              f'свяжитесь с нами.'
    send_mail(subject, message, 'noreply@example.com', [customer_email])
