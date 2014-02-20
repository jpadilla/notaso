import datetime

from django import forms
from django.shortcuts import get_object_or_404

from professors.models import Professor
from .models import Comment


class AddCommentForm(forms.ModelForm):
    responsibility = forms.IntegerField(required=False, min_value=0, max_value=5)
    personality = forms.IntegerField(required=False, min_value=0, max_value=5)
    workload = forms.IntegerField(required=False, min_value=0, max_value=5)
    difficulty = forms.IntegerField(required=False, min_value=0, max_value=5)
    class Meta:
        model = Comment
        fields = ['body', 'is_anonymous', 'responsibility', 'personality', 'workload', 'difficulty']

    def save_form(self, request, prof_slug):
        c = self.save(commit=False)
        c.created_by = request.user
        c.professor = get_object_or_404(Professor, slug=prof_slug) 
        c.created_at = datetime.datetime.today()
        c.save()
