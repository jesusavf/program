BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "salones" (
	"id_salon"	INTEGER NOT NULL,
	"nombre"	VARCHAR(20) NOT NULL,
	PRIMARY KEY("id_salon" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "SQLITEADMIN_QUERIES" (
	"ID"	INTEGER,
	"NAME"	VARCHAR(100),
	"SQL"	TEXT,
	PRIMARY KEY("ID")
);
CREATE TABLE IF NOT EXISTS "habitaciones_servicios" (
	"habitacion_id"	INTEGER,
	"servicio_id"	INTEGER,
	FOREIGN KEY("habitacion_id") REFERENCES "habitaciones"("id_habitacion"),
	FOREIGN KEY("servicio_id") REFERENCES "servicios"("id_servicio")
);
CREATE TABLE IF NOT EXISTS "promociones_habitaciones" (
	"habitacion_id"	INTEGER,
	"promocion_id"	INTEGER,
	FOREIGN KEY("habitacion_id") REFERENCES "habitaciones"("id_habitacion"),
	FOREIGN KEY("promocion_id") REFERENCES "promociones"("id_promocion")
);
CREATE TABLE IF NOT EXISTS "promociones_restaurantes" (
	"restaurante_id"	INTEGER,
	"promocion_id"	INTEGER,
	FOREIGN KEY("restaurante_id") REFERENCES "restaurantes"("id_restaurante"),
	FOREIGN KEY("promocion_id") REFERENCES "promociones"("id_promocion")
);
CREATE TABLE IF NOT EXISTS "configuraciones" (
	"id_configuracion"	INTEGER NOT NULL,
	"nombre"	VARCHAR(30) NOT NULL,
	PRIMARY KEY("id_configuracion")
);
CREATE TABLE IF NOT EXISTS "albercas" (
	"id_alberca"	INTEGER NOT NULL,
	"nombre"	VARCHAR(20) NOT NULL,
	"profundidad"	FLOAT,
	"vestimenta"	VARCHAR(40),
	"dia"	VARCHAR(30),
	"horario"	VARCHAR(30),
	"edad_ingreso"	VARCHAR(30),
	PRIMARY KEY("id_alberca" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "actividades" (
	"id_actividad"	INTEGER NOT NULL,
	"nombre"	VARCHAR(50) NOT NULL,
	"descripcion"	varchar(600) NOT NULL,
	"lugar"	VARCHAR(40),
	"dia"	VARCHAR(30),
	"horario"	VARCHAR(30),
	PRIMARY KEY("id_actividad" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "habitaciones" (
	"id_habitacion"	INTEGER NOT NULL,
	"nombre"	varchar(40) NOT NULL,
	"tipo"	VARCHAR(20) NOT NULL,
	"descripcion"	VARCHAR(500),
	"precio"	FLOAT NOT NULL,
	"tamano_estancia"	VARCHAR(10),
	"cant_personas"	VARCHAR(50),
	"camas_supletorias"	INTEGER,
	"capacidad_maxima"	iNTEGER,
	"camas"	VARCHAR(50),
	PRIMARY KEY("id_habitacion" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "promociones" (
	"id_promocion"	INTEGER NOT NULL,
	"nombre"	VARCHAR(40) NOT NULL,
	"tipo_promo"	VARCHAR(30),
	"descripcion"	VARCHAR(500),
	"precio"	FLOAT NOT NULL,
	"fecha_inicio"	VARCHAR(30) NOT NULL,
	"fecha_fin"	VARCHAR(30) NOT NULL,
	"horario"	VARCHAR(200),
	"dia"	VARCHAR(100),
	PRIMARY KEY("id_promocion" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "servicios" (
	"id_servicio"	INTEGER NOT NULL,
	"nombre"	VARCHAR(40) NOT NULL,
	"descripcion"	VARCHAR(500),
	PRIMARY KEY("id_servicio" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "restaurantes" (
	"id_restaurante"	INTEGER NOT NULL,
	"nombre"	VARCHAR(40) NOT NULL,
	"descripcion"	VARCHAR(500) NOT NULL,
	"tipo"	VARCHAR(30),
	"codigo_de_vestir"	VARCHAR(25),
	"dia"	VARCHAR(30),
	"horario"	VARCHAR(30),
	"edad_ingreso"	VARCHAR(100),
	PRIMARY KEY("id_restaurante" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "vacantes" (
	"id_vacantes"	INTEGER NOT NULL,
	"puesto"	VARCHAR(30) NOT NULL,
	"descripcion"	VARCHAR(500),
	"lugares_disponibles"	INTEGER NOT NULL,
	"salario"	FLOAT,
	"horario"	VARCHAR(30),
	"ubicacion"	VARCHAR(50),
	"rango_edad"	VARCHAR(20),
	"sexo"	VARCHAR(20),
	PRIMARY KEY("id_vacantes" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "configuraciones_salones" (
	"salon_id"	INTEGER,
	"configuracion_id"	INTEGER,
	"cantidad_personas"	INTEGER,
	"precio"	FLOAT,
	"hora_extra"	FLOAT
);
INSERT INTO "salones" VALUES (1,'las haciendas');
INSERT INTO "salones" VALUES (2,'las haciendas II');
INSERT INTO "salones" VALUES (3,'las haciendas III');
INSERT INTO "salones" VALUES (4,'la escondida');
INSERT INTO "salones" VALUES (5,'de la mora');
INSERT INTO "salones" VALUES (6,'la fortuna ');
INSERT INTO "salones" VALUES (7,'compostela');
INSERT INTO "SQLITEADMIN_QUERIES" VALUES (1,'habitaciones_servicios','CREATE TABLE habitaciones_servicios (
    habitacion_id INTEGER,
    servicio_id INTEGER,
    FOREIGN KEY(habitacion_id) REFERENCES habitaciones(id_habitacion),
    FOREIGN KEY(servicio_id) REFERENCES servicios(id_servicio)
);');
INSERT INTO "SQLITEADMIN_QUERIES" VALUES (2,'promociones_habitaciones','CREATE TABLE promociones_habitaciones (
    habitacion_id INTEGER,
    promocion_id INTEGER,
    FOREIGN KEY(habitacion_id) REFERENCES habitaciones(id_habitacion),
    FOREIGN KEY(promocion_id) REFERENCES promociones(id_promocion)
);');
INSERT INTO "SQLITEADMIN_QUERIES" VALUES (3,'promos_rest','CREATE TABLE promociones_restaurantes (
    restaurante_id INTEGER,
    promocion_id INTEGER,
    FOREIGN KEY(restaurante_id) REFERENCES restaurantes(id_restaurante),
    FOREIGN KEY(promocion_id) REFERENCES promociones(id_promocion)
);');
INSERT INTO "SQLITEADMIN_QUERIES" VALUES (4,'configuraciones_salones','CREATE TABLE configuraciones_salones (
    salon_id INTEGER,
    configuracion_id INTEGER,
    cantidad_personas INTEGER,
    precio FLOAT,
    FOREIGN KEY(salon_id) REFERENCES salones(id_salon),
    FOREIGN KEY(configuracion_id) REFERENCES configuraciones(id_configuracion)
);');
INSERT INTO "SQLITEADMIN_QUERIES" VALUES (5,'datos_actividades','INSERT INTO actividades VALUES (null, ''piscina_1'', ''1.40'',''ropa de licra'',''lunes a domingo'', ''09:00am a 10:30pm'',''mayores de 15 a�os'');
INSERT INTO actividades VALUES (null, ''piscina_2'', ''1.68'',''ropa de licra'',''lunes a domingo'',''10:30am a 10:30pm'',''mayores de 18 a�os'');');
INSERT INTO "habitaciones_servicios" VALUES (1,1);
INSERT INTO "habitaciones_servicios" VALUES (1,2);
INSERT INTO "habitaciones_servicios" VALUES (2,1);
INSERT INTO "habitaciones_servicios" VALUES (2,2);
INSERT INTO "habitaciones_servicios" VALUES (2,3);
INSERT INTO "habitaciones_servicios" VALUES (2,4);
INSERT INTO "promociones_habitaciones" VALUES (1,3);
INSERT INTO "promociones_restaurantes" VALUES (1,1);
INSERT INTO "promociones_restaurantes" VALUES (1,2);
INSERT INTO "configuraciones" VALUES (1,'escuela');
INSERT INTO "configuraciones" VALUES (2,'auditorio');
INSERT INTO "configuraciones" VALUES (3,'herradura');
INSERT INTO "configuraciones" VALUES (4,'banquete');
INSERT INTO "albercas" VALUES (1,'piscina_1',1.4,'ropa de licra','lunes a domingo','09:00am a 10:30pm','mayores de 15 a�os');
INSERT INTO "albercas" VALUES (4,'piscina_2',1.68,'ropa de licra','lunes a domingo','10:30am a 10:30pm','mayores de 18 a�os');
INSERT INTO "actividades" VALUES (1,'WOGA','Tambien llamado yoga acu�tico es una t�cnica de ejercicios en el agua teniendo en cuenta la flotaci�n, el equilibrio, la concentraci�n y la respiraci�n. Se puede realizar de forma individual o colectiva','piscina_1','martes y miercoles','10:30 a 11:30');
INSERT INTO "actividades" VALUES (4,'AQUACYCLING','Es una tecnica de entrenamiento f�sico mediante una bicicleta sumergida en la piscina quedando parte del cuerpo al descubierto.','piscina_2','jueves y viernes','10:30 a 11:30');
INSERT INTO "habitaciones" VALUES (1,'estandar ','sencilla','Disfrute del lujo en su m�xima expresi�n en esta hermosa habitaci�n',1250.0,'93 m2','1 persona',1,3,'1 cama matrimonial');
INSERT INTO "habitaciones" VALUES (2,'superior','doble','Ideal para un viaje en pareja o familia.',1350.0,'99 m2','2 adultos y 1 menor',1,4,'1 cama king');
INSERT INTO "promociones" VALUES (1,'desayuno para damas','restaurante','Disfruta de nuestro delicioso Buffet en compa��a de tus Amistades por tan solo 120.00 por persona.',120.0,'3 de agosto del 2019','31 de diciembre del 2019','lunes a viernes de 7:00 am a 12:00 pm, s�bados y domingos de 7:00 am a 1:00 pm','lunes a domingo');
INSERT INTO "promociones" VALUES (2,'buffet adultos','restaurante','disfruta nuestro delicioso buffet de comida mexicana e internacional.',160.0,'permanente','permanente','lunes a viernes de 7:00 am a 12:00 pm, s�bados y domingos de 7:00 am a 1:00 pm','lunes a domingo');
INSERT INTO "promociones" VALUES (3,'san valentin','hotel','30% en habitaciones',659.0,'14 de febrero del 2020','15 de febrero del 2020','todo el dia','14 y 15 de febrero');
INSERT INTO "servicios" VALUES (1,'minibar','minibar surtido diariamente');
INSERT INTO "servicios" VALUES (2,'secadora de cabello',NULL);
INSERT INTO "servicios" VALUES (3,'cafetera',NULL);
INSERT INTO "servicios" VALUES (4,'almohadas y edred�n','Estan hechos de plumas de ganso');
INSERT INTO "restaurantes" VALUES (1,'los cafetales',' Restaurant Los Cafetales te ofrece  de lunes a viernes  caf�, jugos naturales, servicio a la plancha, guisados, frutas de temporada, pan de la casa y los fin de semana menudo, pozole y birria.','internacional','casual','lunes a domingo','7:00 am a 11:00 pm','familiar');
INSERT INTO "vacantes" VALUES (1,'cocinero','Ayudante de chef',2,3500.0,'6:00 am a 1:00 pm','hotel ne-kie','22 a 30','indistinto');
INSERT INTO "vacantes" VALUES (2,'mesero','mesero del restaurante "los cafetales"',4,2000.0,'6:00 am a 1:00 pm','los cafetales','18 a 25','indistinto');
INSERT INTO "configuraciones_salones" VALUES (1,1,700,35000.0,7000.0);
INSERT INTO "configuraciones_salones" VALUES (1,2,1200,35000.0,7000.0);
INSERT INTO "configuraciones_salones" VALUES (1,4,700,35000.0,7000.0);
INSERT INTO "configuraciones_salones" VALUES (2,1,300,25000.0,5000.0);
INSERT INTO "configuraciones_salones" VALUES (2,2,400,25000.0,5000.0);
INSERT INTO "configuraciones_salones" VALUES (2,4,300,25000.0,5000.0);
COMMIT;
