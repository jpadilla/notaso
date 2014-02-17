import datetime

from django import forms
from django.shortcuts import get_object_or_404

from professors.models import Professor
from .models import Comment


class AddCommentForm(forms.ModelForm):
    responsibility = forms.IntegerField(required=False)
    personality = forms.IntegerField(required=False)
    workload = forms.IntegerField(required=False)
    difficulty = forms.IntegerField(required=False)
    class Meta:
        model = Comment
        fields = ['body', 'is_anonymous', 'responsibility', 'personality', 'workload', 'difficulty']

    def save_form(self, request, prof_slug):
        c = self.save(commit=False)
        c.created_by = request.user
        c.professor = get_object_or_404(Professor, slug=prof_slug)
        c.created_at = datetime.datetime.today()
        c.save()
