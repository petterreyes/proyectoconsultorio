from django.db import models

# Create your models here.
class Servicios(models.Model):
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10 ,decimal_places=4)
    estado = models.IntegerField()
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_servicios"
        verbose_name = "servicios"
        verbose_name_plural = "servicios"
        ordering = ['created']

    def __str__(self):
        return self.descripcion