from django.db import models

# Create your models here.
class Medicos(models.Model):
    nombre = models.CharField(blank=False, max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1) #1 si esta activo y 2 si esta eliminado
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_medicos"
        verbose_name = "medicos"
        verbose_name_plural = "medicos"

    def __str__(self):
        return self.apellido + ' ' + self.nombre