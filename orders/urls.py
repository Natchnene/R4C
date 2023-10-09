from django.urls import path

from .views import create_order, RobotListView


urlpatterns = [
    path('', RobotListView.as_view(), name='order'),
    path('create_order/', create_order, name='create_order'),
]
