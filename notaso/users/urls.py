from django.conf.urls import url

from .views import SettingsView

urlpatterns = [url(r"^settings/$", SettingsView.as_view(), name="settings")]
