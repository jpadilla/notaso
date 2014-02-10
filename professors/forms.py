from django import forms

from models import Professor


class AddProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'gender', 'university', 'department']

    def save_form(self, request):
        p = self.save(commit=False)
        p.created_by = request.user
        p.save()
        return p
