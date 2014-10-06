TallerModelado 
Vistas, motor de plantillas, formulario de registros sencillos
==============

Vista 1) 

Formulario para registrar un nuevo empleado, validando los datos en el cliente, y en el servidor, los campos del formulario son : documento,nombre, fecha nacimiento, sueldo,sexo.

 	R:  Es retornada en la plantilla nuevomodelempleado.html
 	
 	Las validaciones del lado del cliente las realiza django al definir el tipo de datos que ingresará el usuario, en 		models.py o en forms.py. La validación del lado del servidor se garantiza al realizar la construccion de la basa de datos (ejecutando el comando de Syncdb) desde el Modelo por medio del "models.py". No hará incompatibilidad en datos de esta manera. 

Vista 2)

Una tabla con los empleados, 5 columnas: documento,nombre, fecha nacimiento, sueldo. sexo (con un icono).

	R: Es retornada en la plantilla empleadoLista.html
	
	Se hace uso del for y el if en los tags al igual que el motor de plantillas al hacer uso del extends de la plantilla principal, para introduccir codigo python se usa {% %}

==============

metodología del framework.
_________________
1. Lee ruta en urls.py

			(TallerModelado / ConsVista / ConsVista /urls.py)
			
2. con lo obtenido va a views.py
			
			(TallerModelado / ConsVista / Aplicacion /views.py)
			
3. Realiza toda la logica de views.py y retorna una plantilla.
			
			(TallerModelado / ConsVista / ConsVista / plantillas /)
			

