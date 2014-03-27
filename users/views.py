from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.urlresolvers import reverse

from users.admin import UserCreationForm
from .forms import UserLoginForm


def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(
            reverse('users:login')
        )
    return render(request, 'users/signup.html', {'form': form})


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    return render(request, 'users/login.html', {'form': form})


def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)

    return HttpResponseRedirect('/')
