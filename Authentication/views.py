from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group , User
from .forms import CreateUserForm

def loginUser(request):
	if request.user.is_authenticated:
		return redirect('Res:dashboard')
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Res:dashboard')
		else:
			request.session['login'] = 'rejected'
			return redirect('Auth:login')
	else:
		return render(request, 'Authentication/Login.html')

def logoutUser(request):
	logout(request)
	return redirect('Main:main')

# @admin_only
# @login_required(login_url='main_login')
# @allowed_users(allowed_roles=['admin'])