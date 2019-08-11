from django import forms
from .models import Laborer, Operator

"""

    There will be two possible jobs, a Laborer and an Operator.
    Each job has its own form, and the data submitted will be
    stored in two separate databases.   
     
"""


class LaborerForm(forms.ModelForm):
    last_name = forms.CharField(max_length='100')
    first_name = forms.CharField(max_length='100')
    email = forms.EmailField()
    resume = forms.FileField(required=False)
    completed_application = forms.FileField()

    class Meta:
        model = Laborer
        fields = ['last_name', 'first_name', 'email', 'resume', 'completed_application']


class OperatorForm(forms.ModelForm):
    last_name = forms.CharField(max_length='100')
    first_name = forms.CharField(max_length='100')
    email = forms.EmailField()
    resume = forms.FileField(required=False)
    completed_application = forms.FileField()

    class Meta:
        model = Operator
        fields = ['last_name', 'first_name', 'email', 'resume', 'completed_application']
