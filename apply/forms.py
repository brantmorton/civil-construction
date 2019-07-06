from django import forms
from .models import Laborer, Operator


class LaborerForm(forms.ModelForm):
    last_name = forms.CharField(max_length='100')
    first_name = forms.CharField(max_length='100')
    email = forms.EmailField()
    resume = forms.FileField(required=False)
    completed_application = forms.FileField()

    class Meta:
        model = Laborer
        fields =['last_name', 'first_name', 'email', 'resume', 'completed_application']


class OperatorForm(forms.ModelForm):
    last_name = forms.CharField(max_length='100')
    first_name = forms.CharField(max_length='100')
    email = forms.EmailField()
    resume = forms.FileField(required=False)
    completed_application = forms.FileField()

    class Meta:
        model = Operator
        fields =['last_name', 'first_name', 'email', 'resume', 'completed_application']