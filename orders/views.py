from django.shortcuts import render
from django.views.generic.list import ListView

from customers.models import Customer
from orders.models import Order
from robots.models import Robot


class RobotListView(ListView):
    model = Robot
    template_name = "order.html"


def create_order(request):
    email = request.POST.get('email')
    robot_serial = request.POST.get('robot_serial')
    customer = Customer(email=email)
    customer.save()
    robot = Robot.objects.filter(serial=robot_serial)
    if robot.exists():
        order = Order(customer=customer, robot_serial=robot_serial)
        order.save()
    else:
        order = Order(customer=customer, robot_serial=robot_serial, wait=True)
        order.save()
    return render(request, "order.html")
