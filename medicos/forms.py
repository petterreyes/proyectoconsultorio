from django import forms
from .models import Medicos, Usuario, Paciente, Dia_atencion, Horario_atencion, Antecedente, Examen
from .models import Consulta, Horario_medico,Reservaciones,Tratamiento, Examen_consulta
from django.forms import ModelForm
from datetime import datetime


class MedicosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model=Medicos
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un apellido',
                    'class': 'form-control'
                }
            ),
            'especialidad': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su especialidad',
                    'class': 'form-control'
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese edad',
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese email',
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select()
        }



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido','cedula','edad','email','sexo','tipousuario']

class PacienteForm(forms.ModelForm):
    #class Meta:
       # model=Paciente
        #fields=['nombre','apellido','fecha_nacimiento','cedula','edad','email','sexo','estado_civil','telefono']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model=Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'class': 'form-control'
                }
            ),
            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese fecha',
                    'class': 'form-control'
                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese edad',
                    'class': 'form-control'
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese cedula',
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese email',
                    'class': 'form-control'
                }
            ),
            'estado_civil': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese estado civil',
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese numero de telefono',
                    'class': 'form-control'
                }
            ),
            'sexo': forms.Select()
        }

class Dia_atencionForm(forms.ModelForm):
   # class Meta:
     #   model=Dia_atencion
      #  fields=['descripcion_dia']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion_dia'].widget.attrs['autofocus'] = True
    class Meta:
        model=Dia_atencion
        fields = '__all__'
        widgets = {
            'descripcion_dia': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese dia',
                    'class': 'form-control'
                }
            ),
        }


class Horario_atencionForm(forms.ModelForm):
    #class Meta:
     #   model=Horario_atencion
      #  fields=['hora_inicio','hora_fin']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hora_inicio'].widget.attrs['autofocus'] = True
    class Meta:
        model=Horario_atencion
        fields = '__all__'
        widgets = {
            'hora_inicio': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese Hora de inicio',
                    'class': 'form-control'
                }
            ),
            'hora_fin': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese Hora de fin',
                    'class': 'form-control'
                }
            ),
        }

class AntecedenteForm(forms.ModelForm):
    #class Meta:
     #   model=Antecedente
      #  fields=['descripcion']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].widget.attrs['autofocus'] = True
    class Meta:
        model=Antecedente
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la descipción',
                    'class': 'form-control'
                }
            ),
        }

class ExamenForm(forms.ModelForm):
    #class Meta:
     #   model=Examen
     #   fields=['nombre_examen']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_examen'].widget.attrs['autofocus'] = True
    class Meta:
        model=Examen
        fields = '__all__'
        widgets = {
            'nombre_examen': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la descipción del examen',
                    'class': 'form-control'
                }
            ),
        }


class ConsultaForm(forms.ModelForm):
    class Meta:
        model=Consulta
        fields=['fecha_consulta','motivoconsulta','medico','paciente']

class Examen_consultaForm(forms.ModelForm):
    class Meta:
        model=Examen_consulta
        fields=['descripcion','consulta','examen']

class Horario_medicoForm(forms.ModelForm):
    class Meta:
        model=Horario_medico
        fields=['medico','dia_atencion','horario_atencion']


class ReservacionesForm(forms.ModelForm):
    class Meta:
        model=Reservaciones
        fields=['fecha_reservacion','fecha_ingreso','estado_reservacion','horario','pacientes','medico']


class TratamientoForm(forms.ModelForm):
    class Meta:
        model=Tratamiento
        fields=['fecha_tratamiento','diagnostico','procedimiento','consulta','medico']
