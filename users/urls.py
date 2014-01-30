from django.conf.urls import patterns, include, url

from users import views

urlpatterns = patterns('',
	url(r'^signup/$', views.register, name='register'),
	url(r'^login/$', views.login, name='login'),
)
