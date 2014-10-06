TallerModelado - Vistas, motor de plantillas, formulario de registros sencillos
==============

Vista 1) 

Formulario para registrar un nuevo empleado, validando los datos en el cliente, y en el servidor, los campos del formulario son : documento,nombre, fecha nacimiento, sueldo,sexo.

Vista 2)

Una tabla con los empleados, 5 columnas: documento,nombre, fecha nacimiento, sueldo. sexo (con un icono).

==============

metodología del framework.
_________________
1. Lee ruta en urls.py

			(TallerModelado / ConsVista / ConsVista /urls.py)
			
2. con lo obtenido va a views.py
			(TallerModelado / ConsVista / Aplicacion /views.py)
			
3. Realiza toda la logica de views.py y retorna una plantilla.
			(TallerModelado / ConsVista / ConsVista / plantillas /)
___________________			

Vista 1: Es retornada en la plantilla nuevomodelempleado.html
vista 2: Es retornada en la plantilla empleadoLista.html
