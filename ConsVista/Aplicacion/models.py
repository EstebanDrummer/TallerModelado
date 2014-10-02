from django.db import models

class Empleado(models.Model):
	documento = models.CharField(blank=True, max_length=100)
	nombre = models.CharField(blank=True, max_length=100)
	fecha_nacimiento = models.DateTimeField(blank=True)
	Sueldo = models.CharField(blank=True, max_length=100)
	Sexo = models.CharField(blank=True, max_length=100)