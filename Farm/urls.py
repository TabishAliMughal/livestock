from django.urls import path , include
from Farm.views import *

app_name = "Farm"

urlpatterns = [
    path('animals/', include('Animals.urls' , namespace='Animals')),
    path('dashboard/', Dashboard , name='Dashboard'),
]