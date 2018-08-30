from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from braces.views import LoginRequiredMixin

from .forms import SettingsForm


class SettingsView(LoginRequiredMixin, FormView):
    template_name = "users/settings.html"
    form_class = SettingsForm

    def get_success_url(self):
        return reverse("users:settings")

    def get_context_data(self, **kwargs):
        if "view" not in kwargs:
            kwargs["view"] = self
        return kwargs

    def get_initial(self):
        initial = {
            "first_name": self.request.user.first_name,
            "last_name": self.request.user.last_name,
        }
        return initial

    def form_valid(self, form):
        form.save_form(self.request.user)
        messages.success(self.request, "Perfil actualizado.")
        return redirect(self.get_success_url())
