from django.urls import path
from Animals.views import *

app_name = "Animals"

urlpatterns = [
    path('list/', List , name='List'),
    path('list/<slug>/', List , name='List'),
    path('detail/<pk>/', Detail , name='Detail'),
    path('create/', Create , name='Create'),
    path('expence/add/<pk>/', AddExpence , name='AddExpence'),
    path('product/add/<pk>/', AddProduct , name='AddProduct'),
    path('animal/group/create/<pk>', CreateAnimalGroup , name='CreateAnimalGroup'),
    path('animal/group/<pk>', AnimalGroup , name='AnimalGroup'),
    path('expence/bulk/add/', BulkExpence , name='BulkExpence'),
    path('expence/bulk/add/<pk>', BulkExpence , name='BulkExpence'),
]