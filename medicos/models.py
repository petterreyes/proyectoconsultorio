from django.db import models

# Create your models here.
class Medicos(models.Model):
    nombre = models.CharField(blank=False, max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1) #1 si esta activo y 2 si esta eliminado
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_medicos"
        verbose_name = "medico"
        verbose_name_plural = "medicos"

    def __str__(self):
        return self.apellido + ' ' + self.nombre



class Usuario(models.Model):
    nombre = models.CharField(blank=False, max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    tipousuario = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)  # 1 si esta activo y 2 si esta eliminado
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_usuario"
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.apellido + ' ' + self.nombre

class Paciente(models.Model):
    nombre = models.CharField(blank=False, max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    cedula = models.CharField(max_length=13)
    edad = models.IntegerField()
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    estado_civil = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_paciente"
        verbose_name = "paciente"
        verbose_name_plural = "pacientes"

    def __str__(self):
        return self.apellido + ' ' + self.nombre


class Dia_atencion(models.Model):
    descripcion_dia = models.CharField(max_length=20)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_dia_atencion"
        verbose_name = "dia_atencion"
        verbose_name_plural = "dia_atenciones"

    def __str__(self):
        return self.descripcion_dia

class Horario_atencion(models.Model):
    hora_inicio = models.CharField(max_length=20)
    hora_fin = models.CharField(max_length=20)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_horario_atencion"
        verbose_name = "horario_atencion"
        verbose_name_plural = "horario_atenciones"

    def __str__(self):
        return self.hora_inicio + ' hasta ' + self.hora_fin

class Antecedente(models.Model):
    descripcion = models.CharField(max_length=200)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_antecedente"
        verbose_name = "antecedente"
        verbose_name_plural = "antecedentes"

    def __str__(self):
        return self.descripcion


class Examen(models.Model):
    nombre_examen = models.CharField(max_length=200)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_examen"
        verbose_name = "examen"
        verbose_name_plural = "examenes"

    def __str__(self):
        return self.nombre_examen


class Consulta(models.Model):
    fecha_consulta = models.DateField('fecha que se realiza la consulta', blank=False, null=False)
    motivoconsulta = models.CharField(max_length=200)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_consulta"
        verbose_name = "consulta"
        verbose_name_plural = "consultas"

    def __str__(self):
        return self.motivoconsulta


class Horario_medico(models.Model):
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    dia_atencion = models.ForeignKey(Dia_atencion, on_delete=models.CASCADE)
    horario_atencion = models.ForeignKey(Horario_atencion, on_delete=models.CASCADE)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_horario_medico"
        verbose_name = "horario_medico"
        verbose_name_plural = "horario_medicos"

