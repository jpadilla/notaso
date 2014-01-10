from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):
	firstname = forms.CharField(max_length=30)
	lastname = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=50)

	GENDER_CHOICES = (
		('MALE', 'M'),
		('FEMALE', 'F'),
	)

	gender = forms.ChoiceField(GENDER_CHOICES)
	#facebook_user_id = forms.CharField(max_length=30)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		_user = super(UserCreationForm, self).save(commit=False)
		_user.set_password(self.cleaned_data["password1"])
		_user.email = self.cleaned_data['email']
		_user.save()

		user_profile = UserProfile()
		user_profile.user = _user
		user_profile.firstname = self.cleaned_data['firstname']
		user_profile.lastname = self.cleaned_data['lastname']
		user_profile.email = _user.email
		user_profile.gender = self.cleaned_data['gender']

		if commit:
			user_profile.save()

		return _user
