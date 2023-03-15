from django.urls import path
from Animals.views import *

app_name = "Animals"

urlpatterns = [
    path('list/', List , name='List'),
    path('create/', Create , name='Create'),
    path('create/<type>', Create , name='Create'),
    path('list/<slug>/', List , name='List'),
    path('detail/<pk>/', Detail , name='Detail'),
    path('group/<pk>', AnimalGroup , name='AnimalGroup'),
    path('expence/add/<pk>/', AddExpence , name='AddExpence'),
    path('product/add/<pk>/', AddProduct , name='AddProduct'),
    path('expence/bulk/add/<pk>', BulkExpence , name='BulkExpence'),
    path('group/create/<pk>', CreateAnimalGroup , name='CreateAnimalGroup'),
]