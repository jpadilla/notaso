from django import forms

from .models import User


class SignupForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        max_length=60,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'autofocus': 'autofocus'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender')

    def save(self, user):
        email = self.cleaned_data['email']
        user.email = email
        user.save()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
