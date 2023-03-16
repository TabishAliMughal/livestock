from django.urls import path
from . import views

app_name = 'Authentication'

urlpatterns = [
	path('login/', views.loginUser, name="Login"),
	path('logout/', views.logoutUser, name="Logout"),
]