from django import forms

from .models import Professor


class AddProfessorForm(forms.ModelForm):
    responsibility = forms.IntegerField(required=True, min_value=0,
                                        max_value=5, widget=forms.HiddenInput()
                                        )
    personality = forms.IntegerField(required=True, min_value=0, max_value=5,
                                     widget=forms.HiddenInput())
    workload = forms.IntegerField(required=True, min_value=0, max_value=5,
                                  widget=forms.HiddenInput())
    difficulty = forms.IntegerField(required=True, min_value=0, max_value=5,
                                    widget=forms.HiddenInput())

    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'gender', 'university',
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
