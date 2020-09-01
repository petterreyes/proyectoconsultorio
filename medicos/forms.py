from django import forms
from .models import Medicos

class MedicosForm(forms.ModelForm):
    class Meta:
        model=Medicos
        fields=['apellido','nombre','edad','email','sexo']