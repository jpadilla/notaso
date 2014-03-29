from django.shortcuts import redirect, render
from django.contrib import auth

from .forms import UserLoginForm, UserCreationForm


def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

    if request.user.is_authenticated():
        return redirect('/')

    form = UserLoginForm(request.POST or None)


def login(request):
    if request.user.is_authenticated():
        return redirect('/')

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

    return render(request, 'users/login.html', {'form': form})


def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return redirect('/')
