from django.db import models

# Create your models here.


class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
