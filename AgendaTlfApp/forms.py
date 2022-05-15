from django import forms
from .models import Agenda

class AgendaFormulario(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "telefono": forms.TextInput(attrs={'class': 'form-control'}),
        }