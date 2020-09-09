from django.contrib import admin
from .models import Medicos, Usuario, Paciente, Dia_atencion, Horario_atencion, Antecedente, Examen
from .models import Consulta, Horario_medico, Reservaciones, Tratamiento, Examen_consulta
# Register your models here.
admin.site.register(Medicos)
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Dia_atencion)
admin.site.register(Horario_atencion)
admin.site.register(Antecedente)
admin.site.register(Examen)
admin.site.register(Consulta)
admin.site.register(Horario_medico)
admin.site.register(Reservaciones)
admin.site.register(Tratamiento)
admin.site.register(Examen_consulta)

