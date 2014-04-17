import datetime
from django import forms

from ..comments.models import Comment
from ..universities.models import University
from ..departments.models import Department
from .models import Professor


class AddProfessorForm(forms.Form):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    responsibility = forms.IntegerField(
        required=True, min_value=0,
        max_value=5, widget=forms.HiddenInput())
    personality = forms.IntegerField(
        required=True, min_value=0,
        max_value=5, widget=forms.HiddenInput())
    workload = forms.IntegerField(
        required=True, min_value=0,
        max_value=5, widget=forms.HiddenInput())
    difficulty = forms.IntegerField(
        required=True, min_value=0,
        max_value=5, widget=forms.HiddenInput())
    first_name = forms.CharField(
        max_length=25,
        label="First name",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=75,
        label="Last name",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(
        label="Gender",        
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))
    university = forms.ModelChoiceField(
        label="University",        
        queryset=University.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="-----------")
    department = forms.ModelChoiceField(
        label="Department",        
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="-----------")
    body = forms.CharField(
        label="Comparte tu opinion",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '7'}))
    is_anonymous = forms.BooleanField(
        required=False,
        label="Enviar anonimamente",
        widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    def save_form(self, request):
        p = Professor()
        p.first_name = self.cleaned_data['first_name']
        p.last_name = self.cleaned_data['last_name']
        p.gender = self.cleaned_data['gender']
        p.university = self.cleaned_data['university']
        p.department = self.cleaned_data['department']
        p.created_by = request.user
        p.save()
        self.save_comment_form(request, p)
        return p
    
    def save_comment_form(self, request, prof):
        c = Comment()
        c.body = self.cleaned_data['body']
        c.is_anonymous = self.cleaned_data['is_anonymous']
        c.workload = self.cleaned_data['workload']
        c.responsibility = self.cleaned_data['responsibility']
        c.personality = self.cleaned_data['personality']
        c.difficulty = self.cleaned_data['difficulty']
        c.created_by = request.user
        c.professor = prof
        c.created_at = datetime.datetime.today()

        if c.workload == 1:
            c.workload = 5
        elif c.workload == 2:
            c.workload = 4
        elif c.workload == 4:
            c.workload = 2
        elif c.workload == 5:
            c.workload = 1

        if c.difficulty == 1:
            c.difficulty = 5
        elif c.difficulty == 2:
            c.difficulty = 4
        elif c.difficulty == 4:
            c.difficulty = 2
        elif c.difficulty == 5:
            c.difficulty = 1

        c.save()
