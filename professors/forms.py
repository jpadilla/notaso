from django import forms
from models import Professor
from users.models import User
from django.shortcuts import get_object_or_404

class AddProfessorForm(forms.ModelForm):
	class Meta:
		model = Professor
		fields = ['name', 'lastname', 'gender', 'university', 'department']

	def save_form(self, user):
		p = self.save(commit = False)
		p.created_by = get_object_or_404(User, email=user)
		p.save()