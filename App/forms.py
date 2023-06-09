from django import forms
from .models import Candidate as CandidateModel

class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateModel
        fields = '__all__'
