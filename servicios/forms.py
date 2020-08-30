from django import forms
from .models import Servicios

class Serviciosform(forms.ModelForm):
    class Meta:
        model=Servicios
        fields=['descripcion','precio']