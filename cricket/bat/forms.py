from django import forms
from bat import models

class Bat_Form(forms.ModelForm):
    class Meta:
        model=models.Bat
        fields=['name','runs','team']
