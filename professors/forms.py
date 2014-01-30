from django.shortcuts import get_object_or_404

from django import forms
from models import Professor
from users.models import User


class AddProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'gender', 'university', 'department']

    def save_form(self, user):
        p = self.save(commit=False)
        p.created_by = get_object_or_404(User, email=user)
        p.save()
        return p
