from django import forms
from .models import SobraMaterial

class SobraMaterialForm(forms.ModelForm):
    class Meta:
        model = SobraMaterial
        fields = ['tipo', 'quantidade', 'unidade', 'status', 'imagem_dispositivo']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    # Campo de upload de imagem
    imagem_dispositivo = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
