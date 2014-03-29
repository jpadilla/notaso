from django.shortcuts import redirect
from users.admin import UserCreationForm
from .forms import UserLoginForm


def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

    if request.user.is_authenticated():
        return redirect('/')

    form = UserLoginForm(request.POST or None)
