from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def loginUser(request):
	if request.user.is_authenticated:
		return redirect('Farm:Dashboard')
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Farm:Dashboard')
		else:
			request.session['login'] = 'rejected'
			return redirect('Auth:Login')
	else:
		return render(request, 'Authentication/Login.html')

def logoutUser(request):
	logout(request)
	return redirect('Main:Main')

# @admin_only
# @login_required(login_url='main_login')
# @allowed_users(allowed_roles=['admin'])