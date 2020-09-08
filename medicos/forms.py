from django import forms
from .models import Medicos, Usuario, Paciente, Dia_atencion, Horario_atencion, Antecedente, Examen
from .models import Consulta

class MedicosForm(forms.ModelForm):
    class Meta:
        model=Medicos
        fields=['apellido','nombre','edad','email','sexo']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre','apellido','cedula','edad','email','sexo','tipousuario']

class PacienteForm(forms.ModelForm):
    class Meta:
        model=Paciente
        fields=['nombre','apellido','fecha_nacimiento','cedula','edad','email','sexo','estado_civil','telefono']

class Dia_atencionForm(forms.ModelForm):
    class Meta:
        model=Dia_atencion
        fields=['descripcion_dia']

class Horario_atencionForm(forms.ModelForm):
    class Meta:
        model=Horario_atencion
        fields=['hora_inicio','hora_fin']

class AntecedenteForm(forms.ModelForm):
    class Meta:
        model=Antecedente
        fields=['descripcion']

class ExamenForm(forms.ModelForm):
    class Meta:
        model=Examen
        fields=['nombre_examen']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model=Consulta
        fields=['fecha_consulta','motivoconsulta','medico','paciente']