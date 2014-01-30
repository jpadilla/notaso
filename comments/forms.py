import datetime

from django import forms
from django.shortcuts import get_object_or_404

from users.models import User
from professors.models import Professor
from .models import Comments


class AddCommentForm(forms.ModelForm):
	responsibility = forms.IntegerField(required=False)
	personality = forms.IntegerField(required=False)
	workload = forms.IntegerField(required=False)
	dificulty = forms.IntegerField(required=False)
	class Meta:
		model = Comments
        fields = ['body', 'is_anonymous', 'responsibility', 'personality', 'workload', 'dificulty']

	def save_form(self, user, prof_id):
		c = self.save(commit=False)
		c.created_by = get_object_or_404(User, email=user)
		c.professor = get_object_or_404(Professor, pk=prof_id)
		c.date = datetime.datetime.today()
		c.save()
