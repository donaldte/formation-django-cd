from typing import Any

from django import forms

from django.contrib.auth.forms import UserChangeForm
from django.forms import EmailField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from .models import DataTest


class DataTestForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    class Meta:
        model = DataTest
        
        fields = ['name', 'description']
        
    
    def clean_name(self): # clean_<fieldname>
        name = self.cleaned_data.get('name')
        if name == "test":
            raise forms.ValidationError("This is not a valid name")
        return name   
    

class DataTesFormWithoutModel(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'name-test',
        'placeholder': 'Enter the name of the dataset file'
    }))
    description = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={
        'rows':10,
        'cols': 100
    }))
    
        