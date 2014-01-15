from django import forms
from models import Comments
from users.models import UserProfile
from professors.models import Professor
from django.shortcuts import get_object_or_404

import datetime

class AddCommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['body', 'is_anonimo', 'responsibility', 'personality', 'workload', 'dificulty']

	def save_form(self, user, prof_id):
		c = self.save(commit = False)
		c.created_by = get_object_or_404(UserProfile, email=user)
		c.professor = get_object_or_404(Professor, pk=prof_id)
		print datetime.datetime.today()
		c.date = datetime.datetime.today()
		c.save()