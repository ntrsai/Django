from django import forms
from book import models
class book(forms.ModelForm):
    class Meta:
        model=models.bookstore
        fields=('name','phone','city','address')