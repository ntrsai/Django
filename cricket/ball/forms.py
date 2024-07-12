from django import forms
from ball import models

class Ball_Form(forms.ModelForm):
    class Meta:
        model=models.Ball
        fields=['name','wickets','team']
