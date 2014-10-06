#encoding:utf-8
from datetime import datetime
from django import forms
from django.contrib.admin import widgets 
from django.forms.extras.widgets import SelectDateWidget
from Aplicacion.models import *


TOPIC_CHOICES = (
    ('F', 'Femenino'),
    ('M', 'Masculino'),
)

class ContactoForm(forms.Form):
	Documento = forms.IntegerField(label='Documento')
	Nombre = forms.CharField(widget=forms.TextInput)
	Fecha_nacimiento = forms.DateField(widget=SelectDateWidget(years=range(1910, datetime.now().year)))
	Sueldo = forms.FloatField(label='Sueldo')
	Sexo = forms.ChoiceField(choices =TOPIC_CHOICES)
	#correo = forms.EmailField(label='Tu correo electrónico')
	#mensaje = forms.CharField(widget=forms.Textarea)

class EmpleadoModelForm(forms.ModelForm):
	fecha_nacimiento = forms.DateField(widget=SelectDateWidget(years=range(1910, datetime.now().year)))
	class Meta:
		model = Empleado
