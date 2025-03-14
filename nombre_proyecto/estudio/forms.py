# forms.py
from django import forms
from .models import Expediente

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ['fecha', 'caratula', 'objeto', 'estado', 'descripcion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'objeto': forms.TextInput(attrs={'maxlength': 100}),
        }