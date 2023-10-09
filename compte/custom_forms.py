from django import forms
from .models import Plan, SubcribePlam

class PlanForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        
        model = Plan
        
        fields = [
            'name',
            'description',
            'price'
        ]
        
        # exclude = [
        #     'created_at',
        #     'updated_at'

        # ]
        
    def clean_name(self): # clean_<field_name>
        name = self.cleaned_data.get('name')
        
        if name == 'abc':
            
            raise forms.ValidationError('name cannot be abc')
        
        return name  
      
 
class PlanForm2(forms.Form):        
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if name == 'abc':
            
            raise forms.ValidationError('name cannot be abc in second form')
        
        return name
        