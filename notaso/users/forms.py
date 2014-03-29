from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=60,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'autofocus': 'autofocus'}))
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def signup(self, request, user):
        email = self.cleaned_data['email']
        user.email = email
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
