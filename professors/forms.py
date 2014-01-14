from django import forms
from models import Professor

class AddProfessorForm(forms.ModelForm):
	created_by = forms.CharField(max_length=35)
	class Meta:
		model = Professor
		fields = ('name', 'lastname', 'gender', 'university', 'department')