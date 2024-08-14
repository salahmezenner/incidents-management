# incidents/urls.py

from django.urls import path
from . import views
from .views import platform_chart

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('get_incidents_data', views.get_incidents_data, name='get_incidents_data'),  
    path('platform-chart/', platform_chart, name='platform_chart'),
]