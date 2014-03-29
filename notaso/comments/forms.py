import datetime

from django import forms
from django.shortcuts import get_object_or_404

from ..professors.models import Professor
from .models import Comment


class AddCommentForm(forms.ModelForm):
    responsibility = forms.IntegerField(required=False,
                                        min_value=0, max_value=5)
    personality = forms.IntegerField(required=False, min_value=0, max_value=5)
    workload = forms.IntegerField(required=False, min_value=0, max_value=5)
    difficulty = forms.IntegerField(required=False, min_value=0, max_value=5)

    class Meta:
        model = Comment
        fields = ['body', 'is_anonymous', 'responsibility', 'personality',
                  'workload', 'difficulty']

    def save_form(self, request, prof_slug):
        c = self.save(commit=False)
        c.created_by = request.user
        c.professor = get_object_or_404(Professor, slug=prof_slug)
        c.created_at = datetime.datetime.today()
        c.save()

    def __init__(self, data=None, *args, **kwargs):
        super(AddCommentForm, self).__init__(data, *args, **kwargs)

        if data:
            rating_set = False

            fields = ['responsibility', 'personality', 'workload', 'difficulty']

            for field in fields:
                if data.get(field):
                    rating_set = True

                if rating_set:
                    self.fields[field].required = True
                    self.fields['body'].required = False
