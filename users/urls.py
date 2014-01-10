from django.conf.urls import patterns, include, url

from users import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^register_user/$', views.register, name='register'),
	url(r'^login/$', views.login, name='login'),
)
