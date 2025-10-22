from django import forms
from .models import SobraMaterial, ImagemDispositivo

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

# Form separado só para upload de imagem individual
class ImagemDispositivoForm(forms.ModelForm):
    class Meta:
        model = ImagemDispositivo
        fields = ['imagem']
        widgets = {
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
