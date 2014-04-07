from django import forms

from .models import Professor


class AddProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'university',
                  'department']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'university': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

    def save_form(self, request):
        p = self.save(commit=False)
        p.created_by = request.user
        p.save()
        return p
