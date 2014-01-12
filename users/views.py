from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

from users.admin import UserCreationForm 
from .models import UserProfile
# Create your views here.

def index(request):
	register_form = UserCreationForm()
	return render(request, 'index.html', {'registerform' : register_form})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('thanks')
	register_form = UserCreationForm()
	return render(request, 'index.html', {'registerform' : register_form})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return HttpResponse("You're loged in.")
		else:
			return HttpResponse("Your username/password is incorrect.")
	
	return render(request, 'login.html')
