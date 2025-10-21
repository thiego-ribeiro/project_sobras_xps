from django import forms
from .models import SobraMaterial

class SobraMaterialForm(forms.ModelForm):
    class Meta:
        model = SobraMaterial
        fields = ['tipo', 'quantidade', 'unidade', 'status']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
