from django import forms
from .models import Applicant


class ApplicationForm(forms.ModelForm):
    name = forms.CharField(max_length='100')
    email = forms.EmailField()
    resume = forms.FileField()

    class Meta:
        model = Applicant
        fields =['name', 'email', 'resume']