from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect (reverse("users:login_view"))

	return render(request, "users/user.html")

def login_view(request):
	template_name = "users/login.html"

	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		print (user, request.POST['username'])

		if user is not None:
			login (request, user)

			return HttpResponseRedirect (reverse("users:index"))
		else:
			return render (request, template_name, {"message": "Invalid credentials"})	

	return render (request, template_name, {})

def logout_view(request):
	logout (request)

	return HttpResponseRedirect (reverse("users:login_view"))