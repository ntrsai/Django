from django import forms
from student_generalform import models
class student_Form(forms.ModelForm):
    class Meta:
        model=models.student
        fields=('name','address','city')