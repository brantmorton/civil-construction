from django import forms
from .models import Laborer, Operator


class LaborerForm(forms.ModelForm):
    name = forms.CharField(max_length='100')
    email = forms.EmailField()
    resume = forms.FileField(required=False)
    completed_application = forms.FileField()

    class Meta:
        model = Laborer
        fields =['name', 'email', 'resume', 'completed_application']


class OperatorForm(forms.ModelForm):
    name = forms.CharField(max_length='100')
    email = forms.EmailField()
    resume = forms.FileField(required=False)
    completed_application = forms.FileField()

    class Meta:
        model = Operator
        fields =['name', 'email', 'resume', 'completed_application']