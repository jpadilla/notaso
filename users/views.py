from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

from users.admin import UserCreationForm
from .models import UserProfile

def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(
            reverse('users:login')
        )

    return render(request, 'users/index.html', {'form' : form})

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
    return render(request, 'users/login.html')
