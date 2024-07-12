from django import forms

class TeacherForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)