from django.urls import path
from Main.views import *

app_name = 'Main'

urlpatterns = [
    path('', MainPage , name='Main'),
]