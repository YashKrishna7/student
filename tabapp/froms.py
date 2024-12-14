from django import forms
from . models import Tables

class TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields= ['first_name','last_name','email','address']