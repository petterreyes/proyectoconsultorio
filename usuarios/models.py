from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "seg_rol"
        verbose_name = "rol"
        verbose_name_plural = "roles"

class RolUsuario(models.Model):
    rol = models.OneToOneField(Rol, on_delete=models.SET_NULL, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "seg_rol_usuario"
        verbose_name = "roles_usuario"
        verbose_name_plural = "roles_usuarios"






