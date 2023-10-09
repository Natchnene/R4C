from django.urls import path

from .services import robots_last_week


urlpatterns = [
    path('data/', robots_last_week, name='robots_data'),
]
