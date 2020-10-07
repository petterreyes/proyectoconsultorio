from django.db import models

# Create your models here.
class Medicos(models.Model):
    nombre = models.CharField(blank=False, max_length=200)
    apellido = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField()
    sexo = models.CharField(max_length=21)
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
        return self.apellido + ' ' + self.nombre + ' ' + self.especialidad



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
    fecha_consulta = models.DateField('Fecha que se realiza la consulta', blank=False, null=False)
    motivoconsulta = models.CharField('Motivo de la Consulta',max_length=200)
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


class Examen_consulta(models.Model):
    descripcion = models.CharField(max_length=200)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_examen_consulta"
        verbose_name = "examen_consulta"
        verbose_name_plural = "examen_consultas"

    def __str__(self):
        return self.descripcion


class Horario_medico(models.Model):
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    dia_atencion = models.ForeignKey(Dia_atencion, on_delete=models.CASCADE)
    horario_atencion = models.ForeignKey(Horario_atencion, on_delete=models.CASCADE)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "horario_medicos"
        verbose_name = "horario_medico"
        verbose_name_plural = "horario_medicos"


class Reservaciones(models.Model):
    fecha_ingreso = models.DateField('fecha que ingresa al sistema', blank=False, null=False)
    fecha_reservacion = models.DateField('fecha que se realiza la reservacion', blank=False, null=False)
    estado_reservacion = models.IntegerField(default=1)  # 1 si esta activo y 2 si esta eliminado
    horario = models.CharField(max_length=20)
    pacientes = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_reservaciones"
        verbose_name = "reservacion"
        verbose_name_plural = "reservaciones"
        ordering = ['-fecha_reservacion']



class Tratamiento(models.Model):
    fecha_tratamiento = models.DateField('fecha que se realiza el tratamiento', blank=False, null=False)
    diagnostico = models.CharField(max_length=200)
    procedimiento = models.CharField(max_length=200)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_tratamiento"
        verbose_name = "tratamiento"
        verbose_name_plural = "tratamientos"

    def __str__(self):
        return self.diagnostico