from django.contrib import admin
from .models import Medicos, Usuario, Paciente, Dia_atencion, Horario_atencion, Antecedente, Examen
from .models import Consulta
# Register your models here.
admin.site.register(Medicos)
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Dia_atencion)
admin.site.register(Horario_atencion)
admin.site.register(Antecedente)
admin.site.register(Examen)
admin.site.register(Consulta)