from django import forms
from .models import Applicant


class ApplicationForm(forms.ModelForm):
    name = forms.CharField(max_length='100')
    email = forms.EmailField()
    resume = forms.FileField(required=False)
    completed_application = forms.FileField()

    class Meta:
        model = Applicant
        fields =['name', 'email', 'resume', 'completed_application']