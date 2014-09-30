from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from Aplicacion.forms import ContactoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

def index(request):
		variable ='';
		return render_to_response('index.html', {'variable':variable}, context_instance=RequestContext(request))

def mensaje(request):
	return HttpResponse("Saludo")

def empleadoLista(request):
	empl1={"documento":"1029384", "nombre":"Pepito Perez", "fecha_nacimiento":"10/12/1967", "Sueldo":"1500000", "Sexo":"Masculino"}
	empl2={"documento":"1039482", "nombre":"Pepa Perez", "fecha_nacimiento":"01/06/1985", "Sueldo":"5500000", "Sexo":"Femenino"}
	variable = [empl1, empl2]
	return render_to_response('empleadoLista.html', {'empleados':variable}, context_instance=RequestContext(request))	
	#return render_to_response('PrincipalMDP.html')


def empleadoNuevo(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo='Mensaje desde prueba'
			#contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
			documento = formulario.cleaned_data['Documento']
			nombre = formulario.cleaned_data['Nombre']
			fecha_nacimiento = formulario.cleaned_data['Fecha_nacimiento']
			Sueldo = formulario.cleaned_data['Sueldo']
			Sexo = formulario.cleaned_data['Sexo']
			return HttpResponseRedirect('/')
			
	else:
		formulario = ContactoForm()
	return render_to_response('nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request)) 












































