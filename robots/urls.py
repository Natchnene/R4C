from django.urls import path

from .views import new_robot


urlpatterns = [
    path('new_robot/', new_robot, name='new_robot')
]