from django.views.generic import FormView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .forms import SettingsForm


class SettingsView(LoginRequiredMixin, FormView):
    template_name = "users/settings.html"
    form_class = SettingsForm

    def get_success_url(self):
        return reverse('settings')

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        return kwargs
