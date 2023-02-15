from django.urls import path
from Farm.views import *

app_name = "Farm"

urlpatterns = [
    path('dashboard/', Dashboard , name='Dashboard'),
]