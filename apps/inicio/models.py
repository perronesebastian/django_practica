from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=50, null = False, blank = False)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)

class Empleado(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateTimeField()
    sueldo = models.DecimalField(max_digits = 10, decimal_places=2, default=10000)
    departamento = models.ForeignKey(Departamento, on_delete=SET_NULL, null=True)
    dni = models.CharField(max_length=8, unique=True)
