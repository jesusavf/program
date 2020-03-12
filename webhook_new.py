# import flask dependencies
#SELECT habitaciones.nombre,habitaciones.tipo,habitaciones.descripcion,habitaciones.precio,habitaciones.tamano_estancia,habitaciones.cant_personas,habitaciones.capacidad_maxima,habitaciones.camas FROM habitaciones
#SELECT vacantes.puesto,vacantes.descripcion,vacantes.lugares_disponibles,vacantes.salario,vacantes.horario,vacantes.rango_edad,vacantes.sexo from vacantes
from flask import Flask, make_response, request, jsonify, render_template
from http import cookies
import requests
import sqlite3
from sqlite3 import Error
import re
import time
from datetime import date
import dialogflow
import requests #modulo de peticiones de python
import json
import pusher
import wikipedia
import random
from unicodedata import normalize #quitar acentos
import pytz #detectar zona horaria
from datetime import datetime #para acceder a la hora del sistema
from money.money import Money
from money.currency import Currency

# ...
# inicilizar flask app
app = Flask(__name__)

# crear una ruta para el webhook
@app.route('/webhook')
def hello():
	from modulo.lib import msj
	msjj=[]
	msjj.append("uno")
	msjj.append("tres")

	return msj(msjj)


db_filename = 'bd_hoteld.s3db'#guardar variables en variable.
	
def results():
	
	#region requerimientos
	from modulo.lib import credenciales_cabeceras,credenciales,origenes,variable
	from modulo.lib import instancia,getsesion,lifetime,custom
	from modulo.lib import variable,texto,imagen,obtenertipoarchivo,variable
	from modulo.lib import msj
	from modulo.lib import enviarimagenes,rndenviarimagenes,enviartarjetas,enviarrespuestasrapidas
	from modulo.lib import enviarvideofacebook,respuestarapidafacebook,enviarurlfacebook,enviarpdf_audio_video

	req    =    request.get_json(force=True)
	
	# En la variable req se guardara la peticion que devolvera datos en formato json, extraidos de dialogflow.
	print(req)
	action =    req.get('queryResult').get('action') # De los datos obtenidos en la variable req, se va a extraer 'action', esta nos ayuda a buscar el intent que necesitamos.
	result =    {} # Se guarda un diccionario vacio en la variable result.
	credenciales(request.authorization["username"],request.authorization["password"],'hotelesproyect','hproyect')
	origen=origenes()
	primaryheader=[]
	primaryheader.append(request.headers["render"])
	primaryheader.append(request.headers["section"])
	headercredencial=[]
	headercredencial.append('Zm9yIHRoaXMgc3lzdGVtIGluIHRoZWVlZWVlZSBob3RlbA')
	headercredencial.append('dGhpcyBpcyBhbiBhcGxpY2F0aW9uIGZvciBhIGhvdGVs')
	credenciales_cabeceras(primaryheader,headercredencial)
	mensaje_error='No hemos podido contactarnos con usted espere un momento, si el error persiste contáctenos al (numero)'
	#endregion
	
	
	#region functions()
	#region functions albercas_()
	def albercas_profundidad(alberca):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('albercas')
		valores_parametros.append('profundidad')
		valores_parametros.append(alberca)
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT albercas.nombre,albercas.profundidad FROM albercas WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(alberca,))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						return custom(msj('La alberca '+vestimenta[0]+" tiene una profundidad  de "+str(vestimenta[1])),'albercas',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)
	def albercas_diasapertura(alberca):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('albercas')
		valores_parametros.append('horario')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
					
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT albercas.nombre,albercas.dia,albercas.horario FROM albercas WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(alberca,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						print(valor)
						mensaje='La alberca '+valor[0]+" tiene un horario de "+valor[1]+" de "+valor[2]
						return custom(msj(mensaje),'albercas',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Up no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		except Error:
			return msj(mensaje_error)
	def albercas_hora(alberca):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('albercas')
		valores_parametros.append('hora')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
					
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT albercas.nombre,albercas.horario FROM albercas WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(alberca,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						print(valor)
						mensaje='La alberca '+valor[0]+" abre de "+valor[1]
						return custom(msj(mensaje),'albercas',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		except Error:
			return msj(mensaje_error)
	def albercas_dias(alberca):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('albercas')
		valores_parametros.append('dias')
		valores_parametros.append(alberca)
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT albercas.nombre,albercas.dia FROM albercas WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(alberca,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje='La alberca '+valor[0]+" abre los días "+valor[1]
						return custom(msj(mensaje),'albercas',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	def albercas_edad_ingreso(alberca):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('albercas')
		valores_parametros.append('edad_ingreso')
		valores_parametros.append(alberca)
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT albercas.nombre,albercas.edad_ingreso FROM albercas WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(alberca,))
				vestimenta=cursor.fetchone()
				print(vestimenta)
				if vestimenta!=None:
					try:
						mensaje='La alberca '+vestimenta[0]+" tiene una edad de ingreso de "+str(vestimenta[1])
						return custom(msj(mensaje),'albercas',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	def alberca_informacion(alberca):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('albercas')
		valores_parametros.append('informacion')
		valores_parametros.append(alberca)
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT albercas.nombre,albercas.edad_ingreso,albercas.dia,albercas.horario,albercas.profundidad,albercas.vestimenta FROM albercas WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(alberca,))
				apertura=cursor.fetchone()
				if apertura!=None:
					try:
						mensaje="Alberca: "+apertura[0]+"\nEdad de ingreso:"+apertura[1]+"\nDías de apertura: "+apertura[2]+"\nHorario: "+apertura[3]+"\nProfundidad: "+str(apertura[4])+"\nVestimenta: "+apertura[5]
						return custom(msj(mensaje),'albercas',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	def alberca_oferta(alberca):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('albercas')
		valores_parametros.append('oferta')
		valores_parametros.append(alberca)
		try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT albercas.nombre,albercas.edad_ingreso,albercas.dia,albercas.horario,albercas.profundidad,albercas.vestimenta FROM albercas WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(alberca,))
					apertura=cursor.fetchone()
					if apertura!=None:
						try:
							mensaje="La alberca "+apertura[0]+" ofrece servicio a personas desde  "+apertura[1]+" con días de apertura de "+apertura[2]+" desde "+apertura[3]+" con una profundidad de "+str(apertura[4])+" la cual lleva una vestimenta "+apertura[5]+"."
							return custom(msj(mensaje),'albercas',2,nombre_parametros,valores_parametros)
						except IndexError:
							return msj(mensaje_error)
					else:
						return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	def alberca_vestimenta(alberca):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('albercas')
		valores_parametros.append('vestimenta')
		valores_parametros.append(alberca)
		try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre,vestimenta FROM albercas WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(alberca,))
					vestimenta=cursor.fetchone()
					if vestimenta!=None:
						try:
							mensaje='La alberca '+vestimenta[0]+" necesita vestimenta: "+vestimenta[1]
							return custom(msj(mensaje),'albercas',2,nombre_parametros,valores_parametros)
						except IndexError:
							return msj(mensaje_error)
					else:
						return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	#endregion
	#region functions restaurantes_()
	def restaurantes_descripcion(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('descripcion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT restaurantes.descripcion FROM restaurantes WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes,))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						mensaje=vestimenta[0]
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def restaurantes_dias(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('dias')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT restaurantes.nombre,restaurantes.dia FROM restaurantes WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes,))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						mensaje="El restaurante "+vestimenta[0]+" abre de "+vestimenta[1]
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Upss no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def restaurantes_edad_ingreso(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('edad_ingreso')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT restaurantes.nombre,restaurantes.edad_ingreso FROM restaurantes WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes,))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						if vestimenta[1].lower()=='familiar':
							mensaje="El restaurante "+vestimenta[0]+" abre para toda la familia."
						else:	
							mensaje="El restaurante "+vestimenta[0]+" abre de las "+vestimenta[1]
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def restaurantes_hora_apertura(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('hora_apertura')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT restaurantes.nombre,restaurantes.horario FROM restaurantes WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes,))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						mensaje="El restaurante "+vestimenta[0]+" abre de las "+vestimenta[1]
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def restaurantes_horario(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('horario')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT restaurantes.nombre,restaurantes.dia,restaurantes.horario FROM restaurantes WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes,))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						mensaje='El restaurante '+vestimenta[0]+" abre el "+vestimenta[1]+" desde las "+vestimenta[2]
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def restaurante_precio(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('precio')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT restaurantes.nombre,restaurantes.tipo FROM restaurantes WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes,))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						mensaje='El restaurante '+vestimenta[0]+"\nDe tipo "+vestimenta[1]
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def restaurantes_vestimenta(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('vestimenta')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT restaurantes.nombre,restaurantes.codigo_de_vestir FROM restaurantes WHERE nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes,))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						mensaje="El restaurante "+vestimenta[0]+" tiene un código de vestimenta "+vestimenta[1]
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def restaurantes_informacion(restaurantes2):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('informacion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT count(nombre) FROM restaurantes WHERE REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(nombre),'á','a'), 'é','e'),'í','i'),'ó','o'),'ú','u'),'à','a'),'ì','i')=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes2.lower(),))
				valor=cursor.fetchone()
				if valor[0]==1:
					query = "SELECT restaurantes.nombre,restaurantes.tipo,restaurantes.descripcion,restaurantes.dia,restaurantes.edad_ingreso,restaurantes.horario FROM restaurantes WHERE REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(nombre),'á','a'), 'é','e'),'í','i'),'ó','o'),'ú','u'),'à','a'),'ì','i')=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(restaurantes2.lower(),))
				else:
					query = "SELECT restaurantes.nombre,restaurantes.tipo,restaurantes.descripcion,restaurantes.dia,restaurantes.edad_ingreso,restaurantes.horario FROM restaurantes WHERE REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(nombre),'á','a'), 'é','e'),'í','i'),'ó','o'),'ú','u'),'à','a'),'ì','i') LIKE ? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,('%'+restaurantes2.lower()+'%',))
				vestimenta=cursor.fetchone()
				if vestimenta!=None:
					try:
						mensaje='El restaurante '+vestimenta[0]+"\nDe tipo "+vestimenta[1]+"\nabre los dias "+vestimenta[3]+" con un horario de "+vestimenta[5]+"\nTiene una edad de ingreso de "+vestimenta[4]+"\nDescripción: \n"+vestimenta[2]
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	
	#region function resaurantes_has_promocion()
	def restaurantes_has_promocion_list(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('restaurantes')
		valores_parametros.append('restaurante_promocion_list')
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT restaurantes.nombre,promociones.nombre FROM restaurantes INNER JOIN promociones_restaurantes ON restaurantes.id_restaurante=promociones_restaurantes.restaurante_id INNER JOIN promociones ON promociones_restaurantes.promocion_id=promociones.id_promocion WHERE restaurantes.nombre=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(restaurantes,))
					respuesta=[]
					for vestimenta in cursor:
						respuesta.append('Promoción '+vestimenta[1])
					if len(respuesta)==0:
						return msj('Lo sentimos pero este restaurante no maneja promociones')
					else:
						return custom(respuestarapidafacebook("dentro de las promociones de este restaurante se encuentran estas opciones.",respuesta,origen,'color'),'restaurantes',4,nombre_parametros,valores_parametros)
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT restaurantes.nombre,promociones.nombre FROM restaurantes INNER JOIN promociones_restaurantes ON restaurantes.id_restaurante=promociones_restaurantes.restaurante_id INNER JOIN promociones ON promociones_restaurantes.promocion_id=promociones.id_promocion WHERE restaurantes.nombre=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(restaurantes,))
					respuesta=""
					contador=1
					for vestimenta in cursor:
						if contador==1:
							respuesta='Promoción: '+vestimenta[1]
						else:
							respuesta='Promoción: '+vestimenta[1]
					if respuesta=="":
						return msj('Lo sentimos pero este restaurante no maneja promociones')
					else:
						mensaje="dentro de las promociones de este restaurante se encuentran estas opciones "+respuesta
						return custom(msj(mensaje),'restaurantes',2,nombre_parametros,valores_parametros)
			except Error:
				return msj(mensaje_error)
	def restaurantes_has_promocion_info(restaurantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('promocion')
		valores_parametros.append('info-promocion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT promociones.nombre,promociones.descripcion,promociones.precio,promociones.fecha_inicio,promociones.fecha_fin,promociones.horario,promociones.dia from promociones WHERE promociones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(restaurantes,))
				respuesta=""
				for vestimenta in cursor:
					respuesta="La promoción "+vestimenta[0]+":\nTiene un costo de "+str(Money(vestimenta[2], Currency.USD).format('en_US'))+" pesos.\nInicia el:"+vestimenta[3]+"\nFinaliza el "+vestimenta[4]+"\nTiene un horario de "+vestimenta[5]+"\nEsta promoción consiste en:\n"+vestimenta[1]
				if respuesta=="":
					return msj('Ups la promoción que esta buscando tal vez no exista.')
				return custom(msj(respuesta),'promociones',2,nombre_parametros,valores_parametros)
		except Error:
			return msj(mensaje_error)
	#endregion
	#endregion
	#region functions promociones()
	def promociones_costo(nombre_promocion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('promocion')
		valores_parametros.append('costo')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT promociones.precio FROM promociones WHERE promociones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(nombre_promocion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						m2=Money(valor[0], Currency.USD).format('en_US')
						mensaje="La promoción "+nombre_promocion+" tiene un costo de "+m2
						return custom(msj(mensaje),'promociones',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def promociones_all_data(nombre_promocion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('promocion')
		valores_parametros.append('all-data')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT promociones.precio,promociones.tipo_promo,promociones.horario,promociones.fecha_inicio,promociones.fecha_fin,promociones.dia FROM promociones WHERE promociones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(nombre_promocion,))
				valor=cursor.fetchone()
				if len(valor)==0:
					return msj('Lo sentimos pero este restaurante no maneja promociones')
				else:
					m2=Money(valor[0], Currency.USD).format('en_US')
					mensaje="La promoción "+nombre_promocion+" tiene un costo de "+m2+" esta promoción esta echa para "+valor[1]+".\nTiene un horario de "+valor[2]+".\nSu fecha de inicio es el "+valor[3]+" y su fecha de finalización es "+valor[4]+".\nLos días "+valor[5]
					return custom(msj(mensaje),'promociones',2,nombre_parametros,valores_parametros)
		except Error:
			return msj(mensaje_error)
	def promociones_descripcion(nombre_promocion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('promocion')
		valores_parametros.append('descripcion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT promociones.descripcion FROM promociones WHERE promociones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(nombre_promocion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="La promoción "+nombre_promocion+" consiste en "+valor[0]
						return custom(msj(mensaje),'promociones',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def promociones_dia(nombre_promocion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('promocion')
		valores_parametros.append('dia')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT promociones.dia FROM promociones WHERE promociones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(nombre_promocion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="La promoción "+nombre_promocion+" abre los días "+valor[0]
						return custom(msj(mensaje),'promociones',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def promociones_fechas(nombre_promocion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('promocion')
		valores_parametros.append('fechas')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT promociones.fecha_inicio,promociones.fecha_fin FROM promociones WHERE promociones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(nombre_promocion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="La promoción "+nombre_promocion+" tiene una fecha de inicio de "+valor[0]+" y una fecha de vencimiento de "+valor[1]
						return custom(msj(mensaje),'promociones',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def promociones_horario(nombre_promocion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('promocion')
		valores_parametros.append('horario')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT promociones.horario FROM promociones WHERE promociones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(nombre_promocion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="La promoción "+nombre_promocion+" tiene un horario de "+valor[0]
						return custom(msj(mensaje),'promociones',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	def promociones_tipo(nombre_promocion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('promocion')
		valores_parametros.append('tipos')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT promociones.tipo_promo FROM promociones WHERE promociones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(nombre_promocion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="La promoción "+nombre_promocion+" esta creada para el "+valor[0]
						return custom(msj(mensaje),'promociones',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		except Error:
			return msj(mensaje_error)
	#endregion
	#region functions salones()
	def salones_capacidad_personas(salones,clasificacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		nombre_parametros.append('clasificacion')
		valores_parametros=[]
		valores_parametros.append('salon')
		valores_parametros.append('capacidad_personas')
		valores_parametros.append(clasificacion)
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "select configuraciones_salones.cantidad_personas FROM configuraciones_salones INNER JOIN salones ON configuraciones_salones.salon_id=salones.id_salon INNER JOIN configuraciones ON configuraciones.id_configuracion=configuraciones_salones.configuracion_id WHERE salones.nombre=? and configuraciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(salones,clasificacion,))
				valor=cursor.fetchone()
				if valor!=None:
					mensaje="El salon " + salones+" para "+clasificacion+" tiene una capacidad de personas de "+str(valor[0])+" personas."
					return custom(msj(mensaje),'salon',2,nombre_parametros,valores_parametros)
				else:
					return msj("No hay ningún resultado.")
		except Error:
				return msj(mensaje_error)
	def salones_hora_extra(salones,clasificacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		nombre_parametros.append('clasificacion')
		valores_parametros=[]
		valores_parametros.append('salon')
		valores_parametros.append('hora_extra')
		valores_parametros.append(clasificacion)
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "select configuraciones_salones.hora_extra FROM configuraciones_salones INNER JOIN salones ON configuraciones_salones.salon_id=salones.id_salon INNER JOIN configuraciones ON configuraciones.id_configuracion=configuraciones_salones.configuracion_id WHERE salones.nombre=? and configuraciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(salones,clasificacion,))
				valor=cursor.fetchone()
				if valor!=None:
					m=Money(valor[0], Currency.USD).format('en_US')
					mensaje="El salon " + salones+" para "+clasificacion+" tiene un precio por hora extra de "+m+"."
					return custom(msj(mensaje),'salon',2,nombre_parametros,valores_parametros)
				else:
					return msj("No hay ningún resultado.")
		except Error:
			return msj(mensaje_error)
	def salones_informacion(salones,clasificacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		nombre_parametros.append('clasificacion')
		valores_parametros=[]
		valores_parametros.append('salon')
		valores_parametros.append('informacion')
		valores_parametros.append(clasificacion)
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "select salones.nombre,configuraciones_salones.cantidad_personas,configuraciones_salones.precio,configuraciones_salones.hora_extra,configuraciones.nombre FROM configuraciones_salones INNER JOIN salones ON configuraciones_salones.salon_id=salones.id_salon INNER JOIN configuraciones ON configuraciones.id_configuracion=configuraciones_salones.configuracion_id WHERE salones.nombre=? LIMIT 4" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(salones,))
				respuesta=""
				primervalor=""
				for registro in cursor:
					if respuesta=="":
						respuesta="El salon " + registro[0]
						primervalor=registro[0]
						m=Money(registro[2], Currency.USD).format('en_US')
						m2=Money(registro[3], Currency.USD).format('en_US')
						respuesta=respuesta+"\n👉tiene una capacidad de personas de \n"+str(registro[1]) +" y maneja tarifas desde "+str(m)+" para "+registro[4]+" con un cobro por hora extra de "+str(m2)
					else:
						respuesta=respuesta+"\n👉tiene una capacidad de personas de \n"+str(registro[1]) +" y maneja tarifas desde "+str(m)+" para "+registro[4]+" con un cobro por hora extra de "+str(m2)
			if respuesta=="":
				return msj("No hay ningún resultado.")
			else:
				return custom(msj(respuesta),'salon',2,nombre_parametros,valores_parametros)
		except Error:
			return msj(mensaje_error)
	def salones_precio(salones,clasificacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		nombre_parametros.append('clasificacion')
		valores_parametros=[]
		valores_parametros.append('salon')
		valores_parametros.append('precio')
		valores_parametros.append(clasificacion)
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "select configuraciones_salones.precio FROM configuraciones_salones INNER JOIN salones ON configuraciones_salones.salon_id=salones.id_salon INNER JOIN configuraciones ON configuraciones.id_configuracion=configuraciones_salones.configuracion_id WHERE salones.nombre=? and configuraciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(salones,clasificacion,))
				valor=cursor.fetchone()
				if valor!=None:
					m=Money(valor[0], Currency.USD).format('en_US')
					mensaje="El salon " + salones+" para "+clasificacion+" tiene un precio de "+m+"."
					return custom(msj(mensaje),'salon',2,nombre_parametros,valores_parametros)
				else:
					return msj("No hay ningún resultado.")
		except Error:
			return msj(mensaje_error)
	#endregion
	#region functions habitaciones()
	def habitaciones_informacion(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('informacion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.tipo,habitaciones.descripcion,habitaciones.precio,habitaciones.tamano_estancia,habitaciones.cant_personas,habitaciones.camas_supletorias,habitaciones.capacidad_maxima,habitaciones.camas FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						moneys=Money(valor[3], Currency.USD).format('en_US')
						mensaje='La habitacion '+valor[0]+" es de tipo "+valor[1]+".\nTiene un costo de "+moneys+".\nCuenta con un tamaño de "+valor[4]+".\nCon una cantidad de personas de "+str(valor[5])+"y capacidad máxima de"+str(valor[7])+".\nCon una cantidad de camas supletorias de "+str(valor[6])+" y un numero de camas de "+str(valor[8])
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)

	def habitaciones_tipo(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('tipo')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.tipo FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje='La habitacion '+valor[0]+" es de tipo "+valor[1]
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)
	
	def habitaciones_descripcion(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('descripcion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.descripcion FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje=valor[1]
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)
	
	def habitaciones_precio(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('precio')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.precio FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						moneys=Money(valor[1], Currency.USD).format('en_US')
						mensaje='La habitacion '+valor[0]+" cuesta "+moneys
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)
	
	def habitaciones_tamano_estancia(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('tamano_estancia')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.tamano_estancia FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje='La habitacion '+valor[0]+" tiene un tamaño de "+valor[1]
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)
	
	def habitaciones_cantidad_personas(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('cantidad_personas')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.cant_personas,habitaciones.capacidad_maxima FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje='La habitacion '+valor[0]+" cuenta con una cantidad de personas de "+str(valor[1])+" y una capacidad máxima de "+str(valor[2])+" personas"
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)
	
	def habitaciones_camas_supletorias(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('camas_supletorias')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.camas_supletorias FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje='La habitacion '+valor[0]+" Cuenta con  "+str(valor[1])+" camas Supletorias"
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)
	
	def habitaciones_capacidad_maxima(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('capacidad_maxima')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.capacidad_maxima FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje='La habitacion '+valor[0]+" tiene una capacidad máxima de "+str(valor[1])+" personas"
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)

	def habitaciones_camas(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('camas')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT habitaciones.nombre,habitaciones.camas,habitaciones.camas_supletorias FROM habitaciones WHERE habitaciones.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(habitacion,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje='La habitacion '+valor[0]+" Cuenta con  "+str(valor[1])+" y "+str(valor[2])+" camas Supletoria "
						return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
				return msj(mensaje_error)
	
	#region habitaciones_has_servicios()
	def habitaciones_has_servicios_list(habitacion):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('restaurante_servicios_list')
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT habitaciones.nombre,servicios.nombre from habitaciones INNER JOIN habitaciones_servicios on habitaciones.id_habitacion=habitaciones_servicios.habitacion_id INNER JOIN servicios on habitaciones_servicios.servicio_id=servicios.id_servicio WHERE habitaciones.nombre=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(habitacion,))
					respuesta=[]
					mensaje="La habitacion "+habitacion+" tiene estos servicios:"
					for valor in cursor:
						respuesta.append(valor[1])
					print(respuesta)
					if len(respuesta)==0:
						return msj("error de proceso")
					else:
						return respuestarapidafacebook(mensaje,respuesta,origen,'color')
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT habitaciones.nombre,servicios.nombre,servicios.descripcion from habitaciones INNER JOIN habitaciones_servicios on habitaciones.id_habitacion=habitaciones_servicios.habitacion_id INNER JOIN servicios on habitaciones_servicios.servicio_id=servicios.id_servicio WHERE habitaciones.nombre=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(habitacion,))
					respuesta=""
					for valor in cursor:
						if respuesta=="":
							respuesta=valor[1]
						else:
							respuesta=respuesta+", "+valor[1]
					if respuesta=="":
						return msj("error de proceso")
					else:
						return msj("La habitacion "+habitacion+" tiene estos servicios: "+respuesta)
			except Error:
				return msj(mensaje_error)
	
	#endregion
	#endregion
	#region servicios
	def servicio_info(servicio):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('servicio')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT servicios.nombre,servicios.descripcion from servicios WHERE servicios.nombre=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(servicio,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						if valor[1]:
							mensaje=valor[1]
							return custom(msj(mensaje),'habitacion',2,nombre_parametros,valores_parametros)
						else:
							return msj("error servicio no encontrado")
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	def servisio_filtro(servicio):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('habitacion')
		valores_parametros.append('servicio')
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT habitaciones.nombre from habitaciones INNER JOIN habitaciones_servicios on habitaciones.id_habitacion=habitaciones_servicios.habitacion_id INNER JOIN servicios on habitaciones_servicios.servicio_id=servicios.id_servicio WHERE servicios.nombre=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(servicio,))
					respuesta=[]
					mensaje="El servicio "+servicio+" tiene estas habitaciones:"
					for valor in cursor:
						respuesta.append(valor[0])
					print(respuesta)
					if len(respuesta)==0:
						return msj("error de proceso")
					else:
						return respuestarapidafacebook(mensaje,respuesta,origen,'color')
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT habitaciones.nombre from habitaciones INNER JOIN habitaciones_servicios on habitaciones.id_habitacion=habitaciones_servicios.habitacion_id INNER JOIN servicios on habitaciones_servicios.servicio_id=servicios.id_servicio WHERE servicios.nombre=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(servicio,))
					respuesta=""
					for valor in cursor:
						if respuesta=="":
							respuesta=valor[0]
						else:
							respuesta=respuesta+", "+valor[0]
					if respuesta=="":
						return msj("error de proceso")
					else:
						return msj("El servicio "+servicio+" tiene estas habitaciones: "+respuesta)
			except Error:
				return msj(mensaje_error)
	#endregion
	#region vacantes()
	def vacantes_informacion(vacantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('vacante')
		valores_parametros.append('informacion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT vacantes.puesto,vacantes.descripcion,vacantes.lugares_disponibles,vacantes.salario,vacantes.horario,vacantes.ubicacion,vacantes.rango_edad,vacantes.sexo from vacantes WHERE vacantes.puesto=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(vacantes,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						moneys=Money(valor[3], Currency.USD).format('en_US')
						mensaje="El puesto "+valor[0]+" que tiene un salario de "+moneys+".\nQue actualmente tiene un cupo de "+str(valor[2])+" esta disponible.\nEste tiene un horario de "+valor[4]+".\nEste se ubica en: "+valor[5]+".\nPara personas de sexo: "+valor[7]+" con una edad de "+valor[6]
						return custom(msj(mensaje),'vacante',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)

	def vacantes_descripcion(vacantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('vacante')
		valores_parametros.append('descripcion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT vacantes.puesto,vacantes.descripcion from vacantes WHERE vacantes.puesto=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(vacantes,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje=valor[1]
						return custom(msj(mensaje),'vacante',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	
	def vacantes_cupo(vacantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('vacante')
		valores_parametros.append('cupo')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT vacantes.puesto,vacantes.lugares_disponibles from vacantes WHERE vacantes.puesto=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(vacantes,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="El puesto "+valor[0]+" actualmente tiene un cupo de "+str(valor[1])
						return custom(msj(mensaje),'vacante',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	
	def vacantes_sueldo(vacantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('vacante')
		valores_parametros.append('salario')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT vacantes.puesto,vacantes.salario from vacantes WHERE vacantes.puesto=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(vacantes,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						moneys=Money(valor[1], Currency.USD).format('en_US')
						mensaje="El puesto "+valor[0]+" que tiene un salario de "+moneys
						return custom(msj(mensaje),'vacante',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	
	def vacantes_horario(vacantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('vacante')
		valores_parametros.append('horario')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT vacantes.puesto,vacantes.horario from vacantes WHERE vacantes.puesto=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(vacantes,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="El puesto "+valor[0]+" tiene un horario de "+valor[1]
						return custom(msj(mensaje),'vacante',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	
	def vacantes_ubicacion(vacantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('vacante')
		valores_parametros.append('ubicacion')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT vacantes.puesto,vacantes.ubicacion from vacantes WHERE vacantes.puesto=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(vacantes,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="El puesto "+valor[0]+" se ubica en "+valor[1]
						return custom(msj(mensaje),'vacante',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	
	def vacantes_rango_edad(vacantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('vacante')
		valores_parametros.append('rango-edad')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT vacantes.puesto,vacantes.rango_edad from vacantes WHERE vacantes.puesto=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(vacantes,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="El puesto "+valor[0]+" maneja un rango de edad de "+valor[1]
						return custom(msj(mensaje),'vacante',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	
	def vacantes_sexo(vacantes):
		nombre_parametros=[]
		nombre_parametros.append('tipo')
		nombre_parametros.append('peticion')
		valores_parametros=[]
		valores_parametros.append('vacante')
		valores_parametros.append('sexo')
		try:
			with sqlite3.connect(db_filename) as conn:#creamos la conección.
				conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
				cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
				query = "SELECT vacantes.puesto,vacantes.sexo from vacantes WHERE vacantes.puesto=? LIMIT 1" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
				cursor.execute(query,(vacantes,))
				valor=cursor.fetchone()
				if valor!=None:
					try:
						mensaje="El puesto "+valor[0]+" es para personas de sexo: "+valor[1]
						return custom(msj(mensaje),'vacante',2,nombre_parametros,valores_parametros)
					except IndexError:
						return msj(mensaje_error)
				else:
					return msj('Posiblemente el nombre este mal por favor vuelva a intentarlo')
		except Error:
			return msj(mensaje_error)
	#endregion
	#endregion
	
	
	#region especial
	if action=='input.unknown':
		return custom(msj('nada'),'alberca',0,'','')
	#endregion
	#region chistes
	if action=="action.chistetoctoc":
		if origen=="FACEBOOK":
			imagen=[]
			imagen.append('https://imgtoboot.000webhostapp.com/jaja.jpg')
			imagen.append('https://imgtoboot.000webhostapp.com/jaja2.png')
			imagen.append('https://imgtoboot.000webhostapp.com/jaja3.jpeg')
			imagen.append('https://imgtoboot.000webhostapp.com/jaja4.jpg')
			mensaje='Jaja que buen chiste.'
			return rndenviarimagenes(imagen,origen,mensaje)
		else:
			mensaje="jaja que buen chiste"
			return msj(mensaje)
	if action=="action.dimechiste":
		chiste={}
		chiste["uno"]="¿Por qué las focas del circo miran siempre hacia arriba?"
	#endregion
	#region facebook welcome_options
	if action=="action.welcome1":
		if origen=='FACEBOOK':
			respuestas=[]
			respuestas.append('Listar albercas')
			respuestas.append('Listar restaurantes')
			respuestas.append('Listar salones')
			return respuestarapidafacebook('Hola buen amigo estoy para servirte desde esta pagina puedes preguntar lo que deses.',respuestas,origen,'color')
		else:
			return msj('Hola buen amigo estoy para servirte desde esta pagina puedes preguntar lo que deses. desde Listar albercas, Listar restaurantes y Listar salones')
	if action=="action.welcome2":
		if origen=='FACEBOOK':
			respuestas=[]
			respuestas.append('Listar albercas')
			respuestas.append('Listar restaurantes')
			respuestas.append('Listar salones')
			return respuestarapidafacebook('Estoy a tu servicio puedes preguntar lo que deses, aunque yo te recomendaría que preguntaras por  estas opciones las cuales son las mas frecuentes.',respuestas,origen,'color')
		else:
			return msj('Estoy a tu servicio puedes preguntar lo que deses, aunque yo te recomendaría que preguntaras por  estas opciones las cuales son las mas frecuentes.')
	if action=="action1.media":
			if obtenertipoarchivo()=='audio':
				print(req.get('originalDetectIntentRequest').get('payload').get('data').get('message').get('mid'))
				#song = AudioSegment.from_mp3(lib.imagen())
				#song.export("mashupdd.wav", format="wav")
				#filename = "mashupdd.wav"
				#r = sr.Recognizer()
				#with sr.AudioFile(filename) as source:
    				# listen for the data (load audio to memory)
					#audio_data = r.record(source)
    				# recognize (convert from speech to text)
					#text = r.recognize_google(audio_data, language="es-US")
					#return lib.msj(text)
				return msj(req.get('originalDetectIntentRequest').get('payload').get('data').get('message').get('mid'))
			else:
				return msj('Ups no he podido comprender lo que me has dicho')
	#endregion
	#region chabotplatica
	#action1.sentement
	if action=="input.welcome":
		if origen=='FACEBOOK':
			respuestas=[]
			respuestas.append('Listar albercas')
			respuestas.append('Listar restaurantes')
			respuestas.append('Listar salones')
			respuestas.append('Listar habitaciones')
			respuestas.append('Listar vacantes')
			respuestas.append('Listar actividades')
			return respuestarapidafacebook('Hola buen amigo estoy para servirte desde esta pagina puedes preguntar lo que deses.',respuestas,origen,'color')
		else:
			return msj('Hola buen amigo estoy para servirte desde esta pagina puedes preguntar lo que deses. desde Listar albercas, Listar restaurantes y Listar salones')

	#if action=="action1.test":
	#	return custom(msj('juas'),'test-followup',2,'caca','salchichas')
	#if action=="action1.testd":
	#	return custom(msj('juas'),'test-followup',0,'','')
	if action=="action.edad":
		if origen=="FACEBOOK":
			url=[]
			url.append('https://imgtoboot.000webhostapp.com/bebe.jpg')
			url.append('https://imgtoboot.000webhostapp.com/bebe2.jpeg')
			url.append('https://imgtoboot.000webhostapp.com/bebe3.jpeg')
			mensajes=[]
			mensajes.append('Apenas soy un bebe que se encuentra en fase beta')
			mensajes.append('Soy apenas un bebe recién nacido')
			return rndenviarimagenes(url,origen,mensajes)

		else:
			mensajes=[]
			mensajes.append('Apenas soy un bebe que se encuentra en fase beta')
			mensajes.append('Soy apenas un bebe recién nacido')
			return msj(mensajes)

	if action=="action.significado":
		palabra=variable('variable1')
		wikipedia.set_lang("es")
		if origen=="FACEBOOK":
			try:
				palabra=wikipedia.summary(palabra,sentences=1)
				return msj(palabra)
			except wikipedia.DisambiguationError as error:
				url={"uno":['visita y aclara tus dudas','https://www.google.com.mx/search?hl=es-419&source=hp&q='+palabra]}
				return enviarurlfacebook('No lo se pero podremos investigar en:',origen,url)
			except wikipedia.exceptions.PageError as error:
				url={"uno":['visita y aclara tus dudas','https://www.google.com.mx/search?hl=es-419&source=hp&q='+palabra]}
				return enviarurlfacebook('No lo se pero podremos investigar en:',origen,url)
		else:
			try:
				palabra=wikipedia.summary(palabra,sentences=1)
				return msj(palabra)
			except wikipedia.DisambiguationError as error:
				return msj('no lo se pero visita y respondera tus dudas https://www.google.com.mx/search?hl=es-419&source=hp&q='+palabra)
			except wikipedia.exceptions.PageError as error:
				return msj('no lo se pero visita y respondera tus dudas https://www.google.com.mx/search?hl=es-419&source=hp&q='+palabra)
		
	if action=="action1.sentement":
		sentiment=variable('sentement')
		if origen=="FACEBOOK":
			if sentiment=='bien':
				text=[]
				text.append('Que bien, que te parecería rentar un hotel para festejar. si/no')
				text.append('Que bueno, deberíamos festejar en un hotel. si/no')
				text.append('Genial, ha que hotel vamos (si/no)')
				img=[]
				img.append('https://imgtoboot.000webhostapp.com/exelente1.jpeg')
				img.append('https://imgtoboot.000webhostapp.com/exelente2.jpg')
				return rndenviarimagenes(img,origen,text)
			if sentiment=='mal':
				text=[]
				text.append('Que mal, deberíamos darnos un respiro en un hotel te interesaría? si/no')
				text.append('Que triste, pero alegrate y date un buen día en un hotel ¿lo desearías? si/no')
				img=[]
				img.append('https://imgtoboot.000webhostapp.com/mal.png')
				img.append('https://imgtoboot.000webhostapp.com/mal2.jpeg')
				img.append('https://imgtoboot.000webhostapp.com/mal3.jpg')
				return rndenviarimagenes(img,origen,text)
				
			
		else:
			if sentiment=='bien':
				text=[]
				text.append('Que bien, que te parecería rentar un hotel para festejar.')
				text.append('Que bueno, deberíamos festejar en un hotel.')
				text.append('Genial, ha que hotel vamos')
				return msj(text)
			if sentiment=='mal':
				text=[]
				text.append('Que mal, deberíamos darnos un respiro en un hotel te interesaría?')
				text.append('Que triste, pero alegrate y date un buen día en un hotel ¿lo desearías?')
				return msj(text)
			else:
				return msj('No he podido entender lo dicho.')
	if action=="action1.triste":
		sentiment=variable('sentement')
		if origen=="FACEBOOK":
			text=[]
			text.append('Que sad se a negado la petición.')
			text.append('Se ha cancelado.')
			img=[]
			img.append('https://imgtoboot.000webhostapp.com/triste.jpeg')
			img.append('https://imgtoboot.000webhostapp.com/triste2.jpg')
			return rndenviarimagenes(img,origen,text)
			
		else:
			text=[]
			text.append('Que sad se a negado la petición.')
			text.append('Se ha cancelado.')
			return msj(text)

	#endregion							
	#region informacion
	if action=="action1.terminos":
		if origen=="FACEBOOK":
			url='https://imgtoboot.000webhostapp.com/terminos_uso.pdf'
			mensaje=[]
			mensaje.append('Los términos de uso se presentan en este documento.')
			mensaje.append('En este documento se encuentran los términos de uso.')
			return enviarpdf_audio_video(url,origen,'document',mensaje)
		else:
			mensaje=[]
			mensaje.append('Para poder visualizar los términos de uso visite esta pagina: https://imgtoboot.000webhostapp.com/terminos_uso.pdf')
			mensaje.append('Dentro de este link se encuentran los términos de uso: https://imgtoboot.000webhostapp.com/terminos_uso.pdf')
			return msj(mensaje)
	#endregion
	#region bd
	#region albercas
	#region albercas parte de las tarjetas
	if action=="action1.listaalberca":
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM albercas LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=1
					lista={}
					for registro in cursor:
						lista[contador]={"boton":[]}
						lista[contador]['titulo']=registro[0]
						lista[contador]['subtitulo']=registro[0]
						lista[contador]['img']='https://imgtoboot.000webhostapp.com/exelente1.jpeg'
						lista[contador]['boton'].append("Ver información de la alberca "+registro[0])
						lista[contador]['boton'].append("Días de apertura de la alberca "+registro[0])
						lista[contador]['boton'].append("Código de vestimenta de la alberca "+registro[0])
						contador=contador+1
					#enviamos la respuesta  al fulfillment de dialogflow
					return enviartarjetas(lista,origen)
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM albercas LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=1
					for registro in cursor:
						if contador==1:
							resp += registro[0]
						else:
							resp += ", "  + registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=2
					#enviamos la respuesta  al fulfillment de dialogflow
					if resp=="":
						msjs="Las habitaciones no existen"
					else:
						msjs='Las habitaciones son: '+resp
					return msj(msjs)
			except Error:
				return msj(mensaje_error)



	if action=="action1.diasapertura":
		if variable('alberca')=='':
			return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		else:
			alberca=variable('alberca')
		if origen=="FACEBOOK":
			return albercas_diasapertura(alberca)
	
		else:
			return albercas_diasapertura(alberca)



	
	
	if action=="action1.vestimentaalberca1":
		if variable('alberca')=='':
			return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		else:
			alberca=variable('alberca')
		if origen=="FACEBOOK":
			return alberca_vestimenta(alberca)
		else:
			return alberca_vestimenta(alberca)

	if action=="action1.albercainfo":
		if variable('alberca')=='':
			return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		else:
			alberca=variable('alberca')
		if origen=="FACEBOOK":
			return alberca_informacion(alberca)
		else:
			return alberca_informacion(alberca)

	if action=="action1.albercaoferta":
		if variable('alberca')=='':
			return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		else:
			alberca=variable('alberca')
		if origen=="FACEBOOK":
			return alberca_oferta(alberca)
		else:
			return alberca_oferta(alberca)

	#endregion

	#region alberca datos

	

	if action=="action1.albercaprofundidad":
		if variable('alberca')=='':
			return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		else:
			alberca=variable('alberca')
		return albercas_profundidad(alberca)

	if action=="action1.edad_ingreso":
		if variable('alberca')=='':
			return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		else:
			alberca=variable('alberca')
		return albercas_edad_ingreso(alberca)



	if action=="action1.albercadias":
		if variable('alberca')=='':
			return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		else:
			alberca=variable('alberca')
		return albercas_dias(alberca)

	if action=="action1.alberca_hora":
		if variable('alberca')=='':
			return msj('Ups no entiendo que a que alberca te refieres.\nPuedes escribir alberca seguido del nombre para recordarlo')
		else:
			alberca=variable('alberca')
		return albercas_hora(alberca)
	#endregion

	#region alberca filtros


	#region alberca filtro1
	if action=="action1.intvestimenta":
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT vestimenta FROM albercas GROUP by vestimenta LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = []#inicializamos variable resp
					for registro in cursor:
						resp.append(registro[0]) #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						#enviamos la respuesta  al fulfillment de dialogflow
					titulo="La alberca de que tipo de vestimenta deseas"
					return custom(respuestarapidafacebook(titulo,resp,origen,"color"),'alberca_filtro-followup',2,'','')
					return custom(msj('tienes una profundidad tal'))
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT vestimenta FROM albercas GROUP by vestimenta LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=1
					for registro in cursor:
						if contador==1:
							resp=resp+" "+registro[0]
						else: 
							resp += ", "  + registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=contador+1
						#enviamos la respuesta  al fulfillment de dialogflow
					msjs='La alberca de que tipo de vestimenta deseas:'+ resp
					return custom(msj(msjs),'alberca_filtro-followup',2,'','')
			except Error:
				return msj(mensaje_error)


	if action=="action2.intprofundida":
		maxima=variable('max')
		minima=variable('min')
		valor=variable('texto')
		variables=[]
		variables.append('min')
		variables.append('max')
		variables.append('texto')
		numeros=[]
		numeros.append(str(minima))
		numeros.append(str(maxima))
		numeros.append(str(valor))
		if origen=="FACEBOOK":
			if minima>maxima:
				return custom(msj('error el dato menor es mayor que el maximo'),'alberca_filtro-followup',0,'','')
				print(req)
			else:
				try:
					with sqlite3.connect(db_filename) as conn:#creamos la conección.
						conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
						cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
						query = "SELECT vestimenta FROM albercas WHERE vestimenta=? and profundidad>=? and profundidad<=?" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
						cursor.execute(query,(valor,minima,maxima,))
						valore=cursor.fetchone()
						print(valore)
						if str(valore)!="None":
							return custom(msj("Desea utilizar un filtro de edad"),'alberca_filtro-custom-followup',2,variables,numeros)
						else:
							conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
							cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
							query = "SELECT vestimenta FROM albercas WHERE vestimenta=?" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
							cursor.execute(query,(valor,))
							valore=cursor.fetchone()
							print(valore)
							if str(valore)!="None":
								return custom(msj('Ninguna alberca coincide con la profundidad deseada.'),'alberca_filtro-followup',0,'','')
							else:
								return custom(msj('No existe esta vestimenta en las albercas'),'alberca_filtro-followup',0,'','')
				except Error:
					return custom(msj(mensaje_error),'alberca_filtro-followup',0,'','')
		else:
			if minima>maxima:
				return custom(msj('error el dato menor es mayor que el maximo'),'alberca_filtro-followup',0,'','')
				print(req)
			else:
				try:
					with sqlite3.connect(db_filename) as conn:#creamos la conección.
						conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
						cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
						query = "SELECT vestimenta FROM albercas WHERE vestimenta=? and profundidad>=? and profundidad<=?" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
						cursor.execute(query,(valor,minima,maxima,))
						valore=cursor.fetchone()
						print(valore)
						if str(valore)!="None":
							return custom(msj("Desea utilizar un filtro de edad"),'alberca_filtro-custom-followup',2,variables,numeros)
						else:
							conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
							cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
							query = "SELECT vestimenta FROM albercas WHERE vestimenta=?" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
							cursor.execute(query,(valor,))
							valore=cursor.fetchone()
							print(valore)
							if str(valore)!="None":
								return custom(msj('Ninguna alberca coincide con la profundidad deseada.'),'alberca_filtro-followup',0,'','')
							else:
								return custom(msj('No existe esta vestimenta en las albercas'),'alberca_filtro-followup',0,'','')
				except Error:
					return custom(msj(mensaje_error),'alberca_filtro-followup',0,'','')


	if action=="action3.profundidadno":
		maxima=variable('max')
		minima=variable('min')
		valor=variable('texto')
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM albercas WHERE vestimenta=? and profundidad>=? and profundidad<=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(valor,minima,maxima,))
					resp = []#inicializamos variable resp
					contador=1
					lista={}
					for registro in cursor:
						resp.append(registro[0])
						lista[contador]={"boton":[]}
						lista[contador]['titulo']=registro[0]
						lista[contador]['subtitulo']=registro[0]
						lista[contador]['img']='https://imgtoboot.000webhostapp.com/exelente1.jpeg'
						lista[contador]['boton'].append("Ver información de "+registro[0])
						lista[contador]['boton'].append("Días de apertura de "+registro[0])
						lista[contador]['boton'].append("Código de vestimenta de "+registro[0])
						#creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=contador+1
					return custom(enviartarjetas(lista,origen),'alberca_filtro-custom-followup',0,'','')
			except Error:
				return custom(msj(mensaje_error),'alberca_filtro-followup',0,'','')
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM albercas WHERE vestimenta=? and profundidad>=? and profundidad<=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(valor,minima,maxima,))
					resp = ""#inicializamos variable resp
					contador=1
					for registro in cursor:
						if contador==1:
							resp=resp+" "+registro[0]
						else: 
							resp += ", "  + registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=contador+1
					return custom(msj('Hoteles disponibles'+resp),'alberca_filtro-custom-followup',0,'','')
			except Error:
				return custom(msj(mensaje_error),'alberca_filtro-followup',0,'','')


	if action=="action3.profundidadsi":
		maxima=variable('max')
		minima=variable('min')
		valor=variable('texto')
		variables=[]
		variables.append('min')
		variables.append('max')
		variables.append('texto')
		numeros=[]
		numeros.append(str(minima))
		numeros.append(str(maxima))
		numeros.append(str(valor))
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT albercas.edad_ingreso FROM albercas GROUP by albercas.edad_ingreso LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)
					resp = []#inicializamos variable resp
					contador=1
					lista={}
					for registro in cursor:
						resp.append(registro[0])
						#creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=contador+1
					return custom(respuestarapidafacebook('Estas son las clasificaciones de edad ',resp,origen,'color'),'alberca_filtro-profundidad-yes-followup',2,variables,numeros)
			except Error:
				return custom(msj(mensaje_error),'alberca_filtro-followup',0,'','')
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT albercas.edad_ingreso FROM albercas GROUP by albercas.edad_ingreso LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)
					resp = ""#inicializamos variable resp
					contador=1
					for registro in cursor:
						if contador==1:
							resp=resp+" "+registro[0]
						else: 
							resp += ", "  + registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=contador+1
					return custom(msj('Estos son los rangos de edad: '+resp),'alberca_filtro-profundidad-yes-followup',2,variables,numeros)
			except Error:
				return custom(msj(mensaje_error),'alberca_filtro-followup',0,'','')

	

	if action=="action4.profundidadsiedad":
		maxima=variable('max')
		minima=variable('min')
		valor=variable('texto')
		edad=variable('edad')
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM albercas WHERE vestimenta=? and profundidad>=? and profundidad<=? and edad_ingreso=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(valor,minima,maxima,edad,))
					resp = []#inicializamos variable resp
					contador=1
					lista={}
					for registro in cursor:
						resp.append(registro[0])
						lista[contador]={"boton":[]}
						lista[contador]['titulo']=registro[0]
						lista[contador]['subtitulo']=registro[0]
						lista[contador]['img']='https://imgtoboot.000webhostapp.com/exelente1.jpeg'
						lista[contador]['boton'].append("Ver información de "+registro[0])
						lista[contador]['boton'].append("Días de apertura de "+registro[0])
						lista[contador]['boton'].append("Código de vestimenta de "+registro[0])
						#creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=contador+1
					return custom(enviartarjetas(lista,origen),'alberca_filtro-profundidad-yes-followup',0,'','')
			except Error:
				return custom(msj(mensaje_error),'alberca_filtro-profundidad-yes-followup',0,'','')
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM albercas WHERE vestimenta=? and profundidad>=? and profundidad<=? and edad_ingreso=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(valor,minima,maxima,edad,))
					resp = ""#inicializamos variable resp
					contador=1
					for registro in cursor:
						if contador==1:
							resp=resp+" "+registro[0]
						else: 
							resp += ", "  + registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=contador+1
					return custom(msj('Hoteles disponibles'+resp),'alberca_filtro-profundidad-yes-followup',0,'','')
			except Error:
				return custom(msj(mensaje_error),'alberca_filtro-profundidad-yes-followup',0,'','')


	#endregion


	#endregion
	#endregion
	##############################################################

	#region salones

	#region salones base
	if action=="action1.saloneslistar":
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM salones LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=0
					lista={}
					for registro in cursor:
						lista[contador]={"boton":[]}
						lista[contador]['titulo']=registro[0]
						lista[contador]['subtitulo']=registro[0]
						lista[contador]['img']='https://imgtoboot.000webhostapp.com/exelente1.jpeg'
						lista[contador]['boton'].append("Ver información del salón "+registro[0])
						lista[contador]['boton'].append("precio del salón "+registro[0])
						lista[contador]['boton'].append("cantidad de personas del salón "+registro[0])
						contador=contador+1
					print(enviartarjetas(lista,origen))
					return enviartarjetas(lista,origen)
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM salones LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=0
					lista={}
					for registro in cursor:
						if resp=="":
							resp=registro[0]
						else:
							resp=resp+", "+registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						#enviamos la respuesta  al fulfillment de dialogflow
					return msj("Escribe el tipo de restaurantes que deseas "+strings)
			except Error:
				return msj(mensaje_error)


	if action=="action1.salon_informacion":
		salones=variable('salon')
		if salones=="":
			return msj('Ups no tengo los criterios para darle una respuesta.\npodría ser que el nombre del salón') 
		if origen=="FACEBOOK":
			return salones_informacion(salones,'todo')
		else:
			return salones_informacion(salones,'todo')

	if action=="action1.salon_capacidad":
		salones=variable('salon')
		clasificacion=variable('clacificacion')
		if salones=="" or clasificacion=="":
			return msj('Ups no tengo los criterios para darle una respuesta.\npodría ser que el nombre del salón o de la clasificación esta mal') 
		if origen=="FACEBOOK":
			return salones_capacidad_personas(salones,clasificacion)
		else:
			return salones_capacidad_personas(salones,clasificacion)
	

	if action=="action1.salon_precio":
		salones=variable('salon')
		clasificacion=variable('clacificacion')
		if salones=="" or clasificacion=="":
			return msj('Ups no tengo los criterios para darle una respuesta.\npodría ser que el nombre del salón o de la clasificación esta mal') 
		if origen=="FACEBOOK":
			return salones_precio(salones,clasificacion)
		else:
			return salones_precio(salones,clasificacion)

	if action=="action1.salon_hora_extra":
		salones=variable('salon')
		clasificacion=variable('clacificacion')
		if salones=="" or clasificacion=="":
			return msj('Ups no tengo los criterios para darle una respuesta.\npodría ser que el nombre del salón o de la clasificación esta mal') 
		if origen=="FACEBOOK":
			return salones_hora_extra(salones,clasificacion)
		else:
			return salones_hora_extra(salones,clasificacion)

	#endregion


	#region salones_configuracion
	if action=="action1.configuracion_salones_info":
		variablebase=variable('configuraciones')
		if variable=="":
			return msj('Ups tal vez esa clasificación de ofertas en salones no exista.')
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "select salones.nombre FROM configuraciones_salones INNER JOIN salones ON configuraciones_salones.salon_id=salones.id_salon INNER JOIN configuraciones ON configuraciones.id_configuracion=configuraciones_salones.configuracion_id WHERE configuraciones.nombre=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(variablebase,))
					resp = []#inicializamos variable resp
					contador=1
					for registro in cursor:
						resp.append(registro[0])
						contador=contador+1
					if len(resp)==0:
						return msj('No hay ningún restaurante con esta tipo de clacificacion')
					else:
						return respuestarapidafacebook('Clasificación '+variablebase+" esta presente en estos salones:",resp,origen,'color')
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "select salones.nombre FROM configuraciones_salones INNER JOIN salones ON configuraciones_salones.salon_id=salones.id_salon INNER JOIN configuraciones ON configuraciones.id_configuracion=configuraciones_salones.configuracion_id WHERE configuraciones.nombre=? LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query,(variablebase,))
					resp = ""#inicializamos variable resp
					contador=1
					for registro in cursor:
						if contador==1:
							resp=resp+" "+registro[0]
						else: 
							resp += ", "  + registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=contador+1
					return msj('Hoteles disponibles'+resp)
			except Error:
				return msj(mensaje_error)
	#endregion

	#endregion


	#region restaurantes


	#region restaurantesbase

	
	if action=="action1.restaurantes_listar":
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM restaurantes LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					lista={}
					contador=0
					for registro in cursor:
						lista[contador]={"boton":[]}
						lista[contador]['titulo']=registro[0]
						lista[contador]['subtitulo']=registro[0]
						lista[contador]['img']='https://imgtoboot.000webhostapp.com/exelente1.jpeg'
						lista[contador]['boton'].append("Ver información de "+registro[0])
						lista[contador]['boton'].append("Que promociones hay en el restaurante "+registro[0])
						lista[contador]['boton'].append("horario del restaurante "+registro[0])
						#enviamos la respuesta  al fulfillment de dialogflow
						contador=contador+1
					return enviartarjetas(lista,origen)
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM restaurantes LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					lista={}
					contador=0
					for registro in cursor:
						if contador==0:
							resp=resp+registro[0]
						else:
							resp=resp+", "+registro[0]
						contador=contador+1
					if resp=="":
						return msj("Ups no existe algún restaurante que pueda mostrarle")
					else:
						return msj('Los restaurantes son: '+resp)
			except Error:
				return msj(mensaje_error)
	
	if action=="action1.restaurante_informacion":
		restaurantes=variable('restaurante')
		restaurantes2=normalize("NFKD",restaurantes).encode("ascii","ignore").decode("ascii")
		if origen=="FACEBOOK":
			return restaurantes_informacion(restaurantes2)
		else:
			return restaurantes_informacion(restaurantes2)

	if action=="action1.restaurante_precios":
		restaurantes=variable('restaurante')
		if restaurantes=="":
			return msj('Ups no he podido entender lo dicho')
		if origen=="FACEBOOK":
			return restaurante_precio(restaurantes)
		else:
			return restaurante_precio(restaurantes)
	
	if action=="action1.resaurante_horario":
		restaurantes=variable('restaurante')
		if restaurantes=="":
			return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		if origen=="FACEBOOK":
			return restaurantes_horario(restaurantes)
		else:
			return restaurantes_horario(restaurantes)


	#endregion

	#region restauranteexra
	if action=="action1.restaurante_descripcion":
		restaurantes=variable('restaurante')
		if restaurantes=="":
			return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		if origen=="FACEBOOK":
			return restaurantes_descripcion(restaurantes)
		else:
			return restaurantes_descripcion(restaurantes)


	if action=="action1.restaurante_vestimenta":
		restaurantes=variable('restaurante')
		if restaurantes=="":
			return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		if origen=="FACEBOOK":
			return restaurantes_vestimenta(restaurantes)
		else:
			return restaurantes_vestimenta(restaurantes)

	if action=="action1.restaurante_dias":
		restaurantes=variable('restaurante')
		if restaurantes=="":
			return msj('Ups no reconozco el restaurante especificado')
		if origen=="FACEBOOK":
			return restaurantes_dias(restaurantes)
		else:
			return restaurantes_dias(restaurantes)

	if action=="action1.restaurante_horas_apertura":
		restaurantes=variable('restaurante')
		if restaurantes=="":
			return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		if origen=="FACEBOOK":
			return restaurantes_hora_apertura(restaurantes)
		else:
			return restaurantes_hora_apertura(restaurantes)

	if action=="action1.restaurante_edad_ingreso":
		restaurantes=variable('restaurante')
		if restaurantes=="":
			return msj('Ups no reconozco el restaurante indicado podrías repetírmelo')
		if origen=="FACEBOOK":
			return restaurantes_edad_ingreso(restaurantes)
		else:
			return restaurantes_edad_ingreso(restaurantes)


	#endregion


	#region restaurante_promociones
	


	if action=="action1.restaurante_has_promociones_list":
		restaurantes=variable('restaurante')
		return restaurantes_has_promocion_list(restaurantes)

	if action=="action1.restaurante_info_promocion_1":
		restaurantes=variable('restaurante')
		if restaurantes=="":
			return msj('Ups la promoción que esta buscando tal vez no exista.')
		return restaurantes_has_promocion_info(restaurantes)

	#endregion
	#endregion


	#region promociones

	#region promociones_list
	if action=="action1.promocion_listar":
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT promociones.nombre FROM promociones LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)
					respuesta=[]
					for vestimenta in cursor:
						respuesta.append(vestimenta[0])
					if len(respuesta)==0:
						return msj('Lo sentimos pero este restaurante no maneja promociones')
					else:
						return respuestarapidafacebook("dentro de las promociones de este restaurante se encuentran estas opciones.",respuesta,origen,'color')		
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT promociones.nombre FROM promociones LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)
					respuesta=""
					contador=1
					for vestimenta in cursor:
						if contador==1:
							respuesta=respuesta+vestimenta[0]
						else:
							respuesta=respuesta+", "+vestimenta[0]
						contador=contador+1
					respuesta="Las promociones existentes son: "+respuesta
					return msj(respuesta)
			except Error:
				return msj(mensaje_error)

	if action=="action1.promocion_all_data":
		nombre_promociones=variable('promociones')
		if origen=="FACEBOOK":
			return promociones_all_data(nombre_promociones)
		else:
			return promociones_all_data(nombre_promociones)


	#end region

	if action=="action1.promocion_tipo":
		nombre_promocion=variable('promociones')
		if origen=="FACEBOOK":
			return promociones_tipo(nombre_promocion)
		else:
			return promociones_tipo(nombre_promocion)


	if action=="action1.promocion_descripcion":
		nombre_promocion=variable('promociones')
		if origen=="FACEBOOK":
			return promociones_descripcion(nombre_promocion)
		else:
			return promociones_descripcion(nombre_promocion)



	if action=="action1.promocio_fechas":
		nombre_promocion=variable('promociones')
		if origen=="FACEBOOK":
			return promociones_fechas(nombre_promocion)
		else:
			return promociones_fechas(nombre_promocion)

	if action=="action1.promocion_horario":
		nombre_promocion=variable('promociones')
		if origen=="FACEBOOK":
			return promociones_horario(nombre_promocion)
		else:
			return promociones_horario(nombre_promocion)

	if action=="action1.promocion_dia":
		nombre_promocion=variable('promociones')
		if origen=="FACEBOOK":
			return promociones_dia(nombre_promocion)
		else:
			return promociones_dia(nombre_promocion)

	if action=="action1.promocion_costo":
		nombre_promocion=variable('promociones')
		if origen=="FACEBOOK":
			return promociones_costo(nombre_promocion)
		else:
			return promociones_costo(nombre_promocion)

	#endregion


	if action=="action2.listarapida":
		if origen=="FACEBOOK":

			respuestas = {"titulo":[],"boton":[]}
			respuestas['titulo'].append('Escribe el tipo de habitación que deseas.')
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM restaurantes" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					for registro in cursor:
						respuestas['boton'].append(registro[0]) #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						#enviamos la respuesta  al fulfillment de dialogflow
					return enviarrespuestasrapidas(respuestas,origen)
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT nombre FROM restaurantes" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					strings=""
					for registro in cursor:
						if strings=="":
							strings=registro[0]
						else:
							strings=strings+", "+registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						#enviamos la respuesta  al fulfillment de dialogflow
					return msj("Escribe el tipo de restaurantes que deseas "+strings)
			except Error:
				return msj(mensaje_error)

	if action=="action3.peticion":
		variable=variable('peticion')
		if origen=="FACEBOOK":
			try:

				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					cursor.execute('SELECT nombre FROM restaurantes WHERE nombre=? LIMIT 1', (variable,))
					strings=""
					for registro in cursor:
						strings=registro[0]
						#enviamos la respuesta  al fulfillment de dialogflow
					return msj(strings)
			except Error:
				return msj(mensaje_error)
		else:
			try:

				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					cursor.execute('SELECT nombre FROM restaurantes WHERE nombre=? LIMIT 1', (variable,))
					strings=""
					for registro in cursor:
						strings=registro[0]
						#enviamos la respuesta  al fulfillment de dialogflow
					if strings=="":
						strings="No existe el restaurante "+variable+"  podría ser por algún error de escritura. \nPuede verificar lo escrito para facilitar su interacción. "
					return msj(strings)
			except Error:
				return msj(mensaje_error)

	#endregion
	#region contexto
	if action=="action1.albercas_contexto":
		tipo=variable('tipo') #esta es para obtener el tipo de elemento
		peticion=variable('peticion')
		alberca=variable('albercas')
		if origen=="FACEBOOK":
			if tipo=="albercas":
				if alberca=="":
					return msj("no encuentro un nombre que coincida con la especificacion que decidio")
				if peticion=="profundidad":
					return albercas_profundidad(alberca)
				elif peticion=="horario":
					return albercas_diasapertura(alberca)
				elif peticion=="dias":
					return albercas_dias(alberca)
				elif peticion=="edad_ingreso":
					return albercas_edad_ingreso(alberca)
				elif peticion=="informacion":
					return alberca_informacion(alberca)
				elif peticion=="oferta":
					return alberca_oferta(alberca)
				elif peticion=="vestimenta":
					return alberca_vestimenta(alberca)
				elif peticion=="hora":
					return albercas_hora(alberca)
				else:
					return msj('error2')
			else:
				return msj('error1')
		else:
			if tipo=="albercas":
				if alberca=="":
					return msj("No encuentro un nombre que coincida con la especificacion que decidio")
				if peticion=="profundidad":
					return albercas_profundidad(alberca)
				elif peticion=="horario":
					return albercas_diasapertura(alberca)
				elif peticion=="dias":
					return albercas_dias(alberca)
				elif peticion=="edad_ingreso":
					return albercas_edad_ingreso(alberca)
				elif peticion=="informacion":
					return alberca_informacion(alberca)
				elif peticion=="oferta":
					return alberca_oferta(alberca)
				elif peticion=="vestimenta":
					return alberca_vestimenta(alberca)
				elif peticion=="hora":
					return albercas_hora(alberca)
				else:
					return msj('error2')
			else:
				return msj('error1')
	if action=="action2.restaurantes_contexto":
		tipo=variable('tipo') #esta es para obtener el tipo de elemento
		peticion=variable('peticion')
		restaurante=variable('restaurante')
		restaurante_limpia=normalize("NFKD",restaurante).encode("ascii","ignore").decode("ascii")
		if restaurante=="":
			return msj("No encuentro un nombre que coincida con la especificacion que decidio")
		if origen=="FACEBOOK":
			if tipo=="restaurantes":
				if peticion=="descripcion":
					return restaurantes_descripcion(restaurante)
				elif peticion=="dias":
					return restaurantes_dias(restaurante)
				elif peticion=="edad_ingreso":
					return restaurantes_edad_ingreso(restaurante)
				elif peticion=="hora_apertura":
					return restaurantes_hora_apertura(restaurante)
				elif peticion=="horario":
					return restaurantes_horario(restaurante)
				elif peticion=="precio":
					return restaurante_precio(restaurante)
				elif peticion=="vestimenta":
					return restaurantes_vestimenta(restaurante)
				elif peticion=="informacion":
					return restaurantes_informacion(restaurante_limpia)
				elif peticion=="restaurante_promocion_list":
					return restaurantes_has_promocion_list(restaurante)
				else:
					return msj('error 2')
			else:
				return msj('error 1')
		else:
			if tipo=="restaurantes":
				if peticion=="descripcion":
					return restaurantes_descripcion(restaurante)
				elif peticion=="dias":
					return restaurantes_dias(restaurante)
				elif peticion=="edad_ingreso":
					return restaurantes_edad_ingreso(restaurante)
				elif peticion=="hora_apertura":
					return restaurantes_hora_apertura(restaurante)
				elif peticion=="horario":
					return restaurantes_horario(restaurante)
				elif peticion=="precio":
					return restaurante_precio(restaurante)
				elif peticion=="vestimenta":
					return restaurantes_vestimenta(restaurante)
				elif peticion=="informacion":
					return restaurantes_informacion(restaurante_limpia)
				elif peticion=="restaurante_promocion_list":
					return restaurantes_has_promocion_list(restaurante)
				else:
					return msj('error 2')
			else:
				return msj('error 1')
	if action=="action2.promocion_costo":
		tipo=variable('tipo') #esta es para obtener el tipo de elemento
		peticion=variable('peticion')
		promociones=variable('promociones')
		if origen=="FACEBOOK":
			if tipo=="promocion":
				if peticion=="costo":
					return promociones_costo(promociones)
				elif peticion=="all-data":
					return promociones_all_data(promociones)
				elif peticion=="descripcion":
					return promociones_descripcion(promociones)
				elif peticion=="dia":
					return promociones_dia(promociones)
				elif peticion=="fechas":
					return promociones_fechas(promociones)
				elif peticion=="horario":
					return promociones_horario(promociones)
				elif peticion=="tipos":
					return promociones_tipo(promociones)
				elif peticion=="info-promocion":
					return restaurantes_has_promocion_info(promociones)
				else:
					return msj('error 2')
			else: 
				return msj('error 1')
		else:
			if tipo=="promocion":
				if peticion=="costo":
					return promociones_costo(promociones)
				elif peticion=="all-data":
					return promociones_all_data(promociones)
				elif peticion=="descripcion":
					return promociones_descripcion(promociones)
				elif peticion=="dia":
					return promociones_dia(promociones)
				elif peticion=="fechas":
					return promociones_fechas(promociones)
				elif peticion=="horario":
					return promociones_horario(promociones)
				elif peticion=="tipos":
					return promociones_tipo(promociones)
				elif peticion=="info-promocion":
					return restaurantes_has_promocion_info(promociones)
				else:
					return msj('error 2')
			else: 
				return msj('error 1')
	if action=="action2.salon_contexto":
		tipo=variable('tipo') #esta es para obtener el tipo de elemento
		peticion=variable('peticion')
		salon=variable('salon')
		clasificacion=variable('clasificacion')
		if action=="FACEBOOK":
			if tipo=="salon":
				if peticion=="capacidad_personas":
					return salones_capacidad_personas(salon,clasificacion)
				elif peticion=="hora_extra":
					return salones_hora_extra(salon,clasificacion)
				elif peticion=="informacion":
					return salones_informacion(salon,'todo')
				elif peticion=="precio":
					return salones_precio(salon,clasificacion)
				else:
					return msj('error 2')
			else:
				return msj('error 1')
		else:
			if tipo=="salon":
				if peticion=="capacidad_personas":
					return salones_capacidad_personas(salon,clasificacion)
				elif peticion=="hora_extra":
					return salones_hora_extra(salon,clasificacion)
				elif peticion=="informacion":
					return salones_informacion(salon,'todo')
				elif peticion=="precio":
					return salones_precio(salon,clasificacion)
				else:
					return msj('error 2')
			else:
				return msj('error 1')
	if action=="action2.habitaciones_contexto":
		tipo=variable('tipo') #esta es para obtener el tipo de elemento
		peticion=variable('peticion')
		habitaciones=variable('habitaciones')
		if origen=="FACEBOOK":
			if tipo=="habitacion":
				if peticion=="informacion":
					return habitaciones_informacion(habitaciones)
				elif peticion=="tipo":
					return habitaciones_tipo(habitaciones)
				elif peticion=="descripcion":
					return habitaciones_descripcion(habitaciones)
				elif peticion=="precio":
					return habitaciones_precio(habitaciones)
				elif peticion=="tamano_estancia":
					return habitaciones_tamano_estancia(habitaciones)
				elif peticion=="cantidad_personas":
					return habitaciones_cantidad_personas(habitaciones)
				elif peticion=="camas_supletorias":
					return habitaciones_camas_supletorias(habitaciones)
				elif peticion=="capacidad_maxima":
					return habitaciones_capacidad_maxima(habitaciones)
				elif peticion=="camas":
					return habitaciones_camas(habitaciones)
				else:
					return msj("error 2")
			else:
				return msj("error 1")
		else:
			if tipo=="habitacion":
				if peticion=="informacion":
					return habitaciones_informacion(habitaciones)
				elif peticion=="tipo":
					return habitaciones_tipo(habitaciones)
				elif peticion=="descripcion":
					return habitaciones_descripcion(habitaciones)
				elif peticion=="precio":
					return habitaciones_precio(habitaciones)
				elif peticion=="tamano_estancia":
					return habitaciones_tamano_estancia(habitaciones)
				elif peticion=="cantidad_personas":
					return habitaciones_cantidad_personas(habitaciones)
				elif peticion=="camas_supletorias":
					return habitaciones_camas_supletorias(habitaciones)
				elif peticion=="capacidad_maxima":
					return habitaciones_capacidad_maxima(habitaciones)
				elif peticion=="camas":
					return habitaciones_camas(habitaciones)
				else:
					return msj("error 2")
			else:
				return msj("error 1")
	if action=="action2.servicios":
		tipo=variable('tipo') #esta es para obtener el tipo de elemento
		peticion=variable('peticion')
		habitaciones_servicios=variable('habitaciones_servicios')
		if origen=="FACEBOOK":
			if tipo=="habitacion":
				if peticion=="servicio":
					return servicio_info(habitaciones_servicios)
				else:
					return('error 2')
			else:
				return msj('error 1')
		else:
			if tipo=="habitacion":
				if peticion=="servicio":
					return servicio_info(habitaciones_servicios)
				else:
					return('error 2')
			else:
				return msj('error 1')
	if action=="action2.vacante_contexto":
		tipo=variable('tipo') #esta es para obtener el tipo de elemento
		peticion=variable('peticion')
		vacantes=variable('vacantes')
		if origen=="FACEBOOK":
			if tipo=="vacante":
				if peticion=="informacion":
					return vacantes_informacion(vacantes)
				elif peticion=="descripcion":
					return vacantes_descripcion(vacantes)
				elif peticion=="cupo":
					return vacantes_cupo(vacantes)
				elif peticion=="salario":
					return vacantes_sueldo(vacantes)
				elif peticion=="horario":
					return vacantes_horario(vacantes)
				elif peticion=="ubicacion":
					return vacantes_ubicacion(vacantes)
				elif peticion=="rango-edad":
					return vacantes_rango_edad(vacantes)
				elif peticion=="sexo":
					return vacantes_sexo(vacantes)
				else:
					return msj("error 2")
			else:
				return msj("error 1")
		else:
			if tipo=="vacante":
				if peticion=="informacion":
					return vacantes_informacion(vacantes)
				elif peticion=="descripcion":
					return vacantes_descripcion(vacantes)
				elif peticion=="cupo":
					return vacantes_cupo(vacantes)
				elif peticion=="salario":
					return vacantes_sueldo(vacantes)
				elif peticion=="horario":
					return vacantes_horario(vacantes)
				elif peticion=="ubicacion":
					return vacantes_ubicacion(vacantes)
				elif peticion=="rango-edad":
					return vacantes_rango_edad(vacantes)
				elif peticion=="sexo":
					return vacantes_sexo(vacantes)
				else:
					return msj("error 2")
			else:
				return msj("error 1")
	#endregion

	#region demas
	#AQUI OBTENEMOS NOMBRE Y DESCRIPCION DE LAS HABITACIONES DEL HOTEL
	if action=="ingresa_action":#ingresa cualquier action para que peruebes esta consulta.
		with sqlite3.connect(db_filename) as conn:
			conn.text_factory 	= lambda b: b.decode(errors = 'ignore')
			cursor = conn.cursor()
			query = "SELECT nombre,descripcion FROM habitaciones"
			cursor.execute(query)
			resp = ""
			for registro in cursor:
				resp+="Tipo de habitación "+registro[0]+":\n"+registro[1]
			result["fulfillmentText"] = resp
			result = jsonify(result)
			return make_response(result)
	#AQUI OBTENEMOS NOMBRE DE LA HABITACION Y NOMBRE DELOS SERVICIOS QUE CONTIENEN(DE UNA TABLA PIVOTE DE LA BD).
	if action=="action3.astros":#ingresa cualquier action para que peruebes esta consulta.
		with sqlite3.connect(db_filename) as conn:
			conn.text_factory 	= lambda b: b.decode(errors = 'ignore')
			cursor = conn.cursor()
			query = "SELECT h.nombre, s.nombre FROM habitaciones_servicios hs INNER JOIN habitaciones h ON hs.habitacion_id = h.id_habitacion INNER JOIN servicios s ON hs.servicio_id = s.id_servicio"
			cursor.execute(query)
			resp = ""
			for registro in cursor:
				resp+="Tipo de habitación "+registro[0]+":\n"+registro[1]
			result["fulfillmentText"] = resp
			result = jsonify(result)
			return make_response(result)
	#endregion

	#region vacantes
	if action=="action1.vacantes_listar":
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT vacantes.puesto from vacantes LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=1
					lista={}
					for registro in cursor:
						lista[contador]={"boton":[]}
						lista[contador]['titulo']=registro[0]
						lista[contador]['subtitulo']=registro[0]
						lista[contador]['img']='https://imgtoboot.000webhostapp.com/exelente1.jpeg'
						lista[contador]['boton'].append("Ver información de la vacante "+registro[0])
						lista[contador]['boton'].append("Donde se ubica el puesto "+registro[0])
						lista[contador]['boton'].append("Sexo del puesto "+registro[0])
						contador=contador+1
					#enviamos la respuesta  al fulfillment de dialogflow
					return enviartarjetas(lista,origen)
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT vacantes.puesto from vacantes LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=1
					for registro in cursor:
						if contador==1:
							resp += registro[0]
						else:
							resp += ", "  + registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=2
					#enviamos la respuesta  al fulfillment de dialogflow
					if resp=="":
						msjs="Las habitaciones no existen"
					else:
						msjs='Las habitaciones son: '+resp
					return msj(msjs)
			except Error:
				return msj(mensaje_error)
	if action=="action1.vacante_informacion":
		vacantes=variable('vacantes')
		if vacantes=="":
			return msj("error")
		return vacantes_informacion(vacantes)

	if action=="action1.vacantes_descripcion":
		vacantes=variable('vacantes')
		if vacantes=="":
			return msj("error")
		return vacantes_descripcion(vacantes)

	if action=="action1.vacantes_cupo":
		vacantes=variable('vacantes')
		if vacantes=="":
			return msj("error")
		return vacantes_cupo(vacantes)
	
	if action=="action1.vacantes_salario":
		vacantes=variable('vacantes')
		if vacantes=="":
			return msj("error")
		return vacantes_sueldo(vacantes)
	
	if action=="action1.vacantes_horario":
		vacantes=variable('vacantes')
		if vacantes=="":
			return msj("error")
		return vacantes_horario(vacantes)
	
	if action=="action1.vacantes_ubicacion":
		vacantes=variable('vacantes')
		if vacantes=="":
			return msj("error")
		return vacantes_ubicacion(vacantes)

	if action=="action1.vacantes_rango_edad":
		vacantes=variable('vacantes')
		if vacantes=="":
			return msj("error")
		return vacantes_rango_edad(vacantes)
	
	if action=="action1.vacantes_sexo":
		vacantes=variable('vacantes')
		if vacantes=="":
			return msj("error")
		return vacantes_sexo(vacantes)
	#endregion	

	#region habitaciones
	if action=="action1.habitaciones_listar":
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT habitaciones.nombre FROM habitaciones LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=0
					lista={}
					for registro in cursor:
						lista[contador]={"boton":[]}
						lista[contador]['titulo']=registro[0]
						lista[contador]['subtitulo']=registro[0]
						lista[contador]['img']='https://imgtoboot.000webhostapp.com/exelente1.jpeg'
						lista[contador]['boton'].append("Ver información de habitacion "+registro[0])
						lista[contador]['boton'].append("precio de habitacion "+registro[0])
						lista[contador]['boton'].append("Servicios de "+registro[0])
						contador=contador+1
					return enviartarjetas(lista,origen)
			except Error:
				return msj(mensaje_error)
		else:
			return msj('habitaciones defauld')

	if action=="action1.habitaciones_informacion":
		habitacion=variable('habitaciones')
		return habitaciones_informacion(habitacion)

	if action=="action1_habitaciones_tipo":
		habitacion=variable('habitaciones')
		return habitaciones_tipo(habitacion)

	if action=="action1.habitaciones_descripcion":
		habitacion=variable('habitaciones')
		return habitaciones_descripcion(habitacion)

	
	if action=="action1_habitacion_precio":
		habitacion=variable('habitaciones')
		return habitaciones_precio(habitacion)
	
	if action=="action1.habitacion_tamano_estancia":
		habitacion=variable('habitaciones')
		return habitaciones_tamano_estancia(habitacion)

	if action=="action1.habitaciones_cantidad_personas":
		habitacion=variable('habitaciones')
		return habitaciones_cantidad_personas(habitacion)

	if action=="action1.habitaciones_camas_supletorias":
		habitacion=variable('habitaciones')
		return habitaciones_camas_supletorias(habitacion)

	if action=="action1.habitaciones_capacidad_maxima":
		habitacion=variable('habitaciones')
		return habitaciones_capacidad_maxima(habitacion)

	if action=="action1.habitaciones_camas":
		habitacion=variable('habitaciones')
		return habitaciones_camas(habitacion)
	
	if action=="action1.habitaciones_has_servicios_list":
		habitacion=variable('habitaciones')
		return habitaciones_has_servicios_list(habitacion)
	#endregion

	#region servicios
	if action=="action1_servicios_info":
		habitaciones_servicios=variable('habitaciones_servicios')
		return servicio_info(habitaciones_servicios)

	if action=="action1.servicios_filtro":
		habitaciones_servicios=variable('habitaciones_servicios')
		return servisio_filtro(habitaciones_servicios)
	#endregion

	#region actividades
	if action=="action1.actividad_listar":
		if origen=="FACEBOOK":
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT actividades.nombre FROM actividades LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=1
					lista={}
					for registro in cursor:
						lista[contador]={"boton":[]}
						lista[contador]['titulo']=registro[0]
						lista[contador]['subtitulo']=registro[0]
						lista[contador]['img']='https://imgtoboot.000webhostapp.com/exelente1.jpeg'
						lista[contador]['boton'].append("Ver información de la actividad "+registro[0])
						lista[contador]['boton'].append("Donde se ubica el actividad "+registro[0])
						lista[contador]['boton'].append("Sexo del actividad "+registro[0])
						contador=contador+1
					#enviamos la respuesta  al fulfillment de dialogflow
					return enviartarjetas(lista,origen)
			except Error:
				return msj(mensaje_error)
		else:
			try:
				with sqlite3.connect(db_filename) as conn:#creamos la conección.
					conn.text_factory 	= lambda b: b.decode(errors = 'ignore')#esta linea ignora las letras con caracteres especiales, las elimina, esto se hace por que es una versin de prueba.
					cursor = conn.cursor() #creamos cursor(Un cursor es el nombre para un área memoria privada que contiene información procedente de la ejecución de una sentencia SELECT. para mas informacion accede al siguiente enlace https://elbauldelprogramador.com/plsql-cursores/ ).
					query = "SELECT actividades.nombre FROM actividades LIMIT 5" #creamos query para obtener el nombre de las habitaciones con las que cuenta el hotel.
					cursor.execute(query)#ejecutamos el query.
					resp = ""#inicializamos variable resp
					contador=1
					for registro in cursor:
						if contador==1:
							resp += registro[0]
						else:
							resp += ", "  + registro[0] #creamos un bucle para recuperar cada una de las filas, en este caso solo es una.
						contador=2
					#enviamos la respuesta  al fulfillment de dialogflow
					if resp=="":
						msjs="Las habitaciones no existen"
					else:
						msjs='Las habitaciones son: '+resp
					return msj(msjs)
			except Error:
				return msj(mensaje_error)
	#endregion

# creando ruta para que interactue con dialogflow
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	# devolver respuesta
	return ''
@app.route('/webhook/<name>', methods=['GET', 'POST'])
def intent(name):
	if name=='2bc73f7c168d61bcabd06d60abbe45e5':
		return results()
	else:
		return 'Error do not exist this directori'


@app.route('/webhook', methods=['PUT', 'PATCH','DELETE','COPY','HEAD','OPTIONS','LINK','UNLINK','PURGE','LOCK','UNLOCK','PROPFIND','VIEW'])
def evitarinjection():
	# devolver respuesta
	return ''


# correr la app
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080,debug=True)