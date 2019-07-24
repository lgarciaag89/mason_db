from django.db import models

from .validators import *
# Create your models here.

class Provincia(models.Model):
    nombre_provincia = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nombre_provincia


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=20, blank=False)
    provincia = models.ForeignKey(Provincia, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_municipio + ',' + self.provincia.nombre_provincia


class Logia(models.Model):
    cod_secretaria = models.CharField(max_length=15, unique=True, blank=False)
    cod_tesoreria = models.CharField(max_length=15, unique=True, blank=False)
    nombre_logia = models.CharField(max_length=20, blank=False)
    direccion = models.TextField(blank=False)
    municipio = models.ForeignKey(Municipio, blank=False, null=False, on_delete=models.CASCADE)
    fecha_fund = models.DateField(validators=[validar_fecha_en_pasado])
    dias_seccion = models.CharField(max_length=50, blank=False)
    hora_seccion = models.TimeField()
    cuenta_bancaria = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        verbose_name_plural = 'Logias'

    def __str__(self):
        return self.nombre_logia
