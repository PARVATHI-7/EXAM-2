from django import forms
from Violation.models import Violation

class ViolationForm(forms.ModelForm):
    class Meta:
        model=Violation
        fields=["description","image"]
