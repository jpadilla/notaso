from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib import messages

from braces.views import LoginRequiredMixin

from .forms import SettingsForm


class SettingsView(LoginRequiredMixin, FormView):
    template_name = "users/settings.html"
    form_class = SettingsForm

    def get_success_url(self):
        return reverse('users:settings')

    def get_initial(self):
        initial = {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email,
        }
        return initial

    def form_valid(self, form):
        form.save_form(self.request.user)
        messages.success(self.request, 'Perfil actualizado.')
        return redirect(self.get_success_url())
