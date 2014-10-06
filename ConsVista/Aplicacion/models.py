from django.db import models

TOPIC_CHOICES = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
)

class Empleado(models.Model):
	documento = models.IntegerField(blank=False, max_length=100)
	nombre = models.CharField(blank=False, max_length=100)
	fecha_nacimiento = models.DateTimeField(blank=False)
	Sueldo = models.IntegerField(blank=False, max_length=100)
	Sexo = models.CharField(blank=False, max_length=100,  choices=TOPIC_CHOICES)

	def __unicode__(self):
		return self.nombre