from flask import request, jsonify
import random
#region autentificaciones
#credenciales es un metodo de verificacion de la aplicacion para poder gestionar las entradas
    #si deseas usarlas vete a dialogflow en la seccion Basic auth escribe el usuario y contraseña que deses
    #luego en el python que se creo importa la libreria con:
    #import lib // la cual es el nombre de la libreria
    #despues por ultimo pon este codigo
    # lib.credenciales(request.authorization["username"],request.authorization["password"],'usuario','contraseña') para eso necesitaras instalar request
def credenciales(user,passw,vuno,vdos):
    if user==vuno: #comparo los usuarios
        if passw==vdos: #comparo las contraseñas
            return True #regreso un valor para prosegir
        else:
            exit() #saco del programa si no pasa las autentificaciones
    else:
        exit() #saco del programa si no pasa las autentificaciones

#este es parecido pero tiene una utilidad  mas avanzada pero esta es manejada por arrays
    #vasta con poner valocabeceras=[request.headers["nombre de header"],request.headers["nombre de header 2"]] y se almacenaran o tambien se puede usar
    #valocabeceras=[]
    #valorcabeceras.append(request.headers["nombre de header"])
    #valorcabeceras.append(request.headers["nombre de header 2"])
    #esto anexara los datos
    #para los datos ocupamos otro array el cual funciona para la comparacion
    #valordato=[]
    #valordato.append('valor del header 1')
    #valordato.append('valor del header 2')
    #posteriormente las llamamos con lib.credenciales_cabeceras(valorcabeceras,valordato)
def credenciales_cabeceras(headers,datos):
    if type(headers)==list:
        estado=True #accedo a un valor inicial de verdadero al acceso del usuario
        if len(headers)== len(datos): #comparo el numero de elementos del array para ver si hay una diferencia sacarlo directamente de la aplicacion
            contador=1 #creo un contador
            while contador<=len(headers): #creo un while o contador para acceder a cada elemento del array
                if headers[contador-1]==datos[contador-1] and estado==True: #compara los elementos del array
                    estado=True #regreso un valor a la variable de autentificacion true
                else:
                    estado=False #regreso un valor a la variable de autentificacion false
                contador=contador+1 #agrego valor al contador
            if estado==True:
                return True#regreso un valor para prosegir
            else:
                exit()#saco del programa si no pasa las autentificaciones
        else:
            exit()#saco del programa si no pasa las autentificaciones
    elif type(headers)==dict:
        estado=True #accedo a un valor inicial de verdadero al acceso del usuario
        if len(headers)== len(datos): #comparo el numero de elementos del array para ver si hay una diferencia sacarlo directamente de la aplicacion
            for head in headers: #cuenta los elementos
                if headers[head]==datos[head] and estado==True: #compara los elementos del diccionario
                    estado=True #devuelve un balor true
                else:
                    exit() #sale del elemento por falta de autentificacion
        else:
            exit() #sale del elemento por falta de autentificacion
    else:
        if headers==datos: #comparo el valor de los header
            return True #regreso un valor para prosegir
        else:
            exit() #saco del programa si no pasa las autentificaciones

#endregion
    
#region obtener
#region obtener_requerimientos
#esta es una forma de observar el origen del envio de datos ya se FACEBOOK, TWITER entre otros debolviendo una cadena
    #para usarlo vasta con usar lib.origenes() el cual regresara un valor de acuerdo a la plataforma
    #una forma de usarlo seria
    #valordeorigen=lib.origenes() //FACEBOOK
    #if valordeorigen=='FACEBOOK': //lo que deses
    #else: //por ende se mandara mensajes defauld los cuales seran para las demas plataformas
def origenes():
    req = request.get_json(force=True) #combierto los valores en un json
    if req.get("originalDetectIntentRequest").get("payload").get("source"): #compruebo si existen
        return (req.get("originalDetectIntentRequest").get("payload").get("source").upper()) #si existen los combierto a mayusculas
    else:
        frase = u'indefinido'
        return frase.upper() #devuelvo el valor INDEFINIDO si no se encuentra ninguna plataforma

#como tal se parese a origenes pero esta tiene como objetivo el de tomar el nombre de las instancias para compararlo
    #ejemplo
    # if lib.instancia('nombre de la instancia'):
def instancia(nombre):
    req = request.get_json(force=True) #combierto los valores en un json
    if req.get('queryResult').get('intent').get('displayName')==nombre: #verifico su existencia
        return True #regreso valor True si es verdad
    else:
        return False #regreso valor False si es falso

def getsesion(): #accede a la session de dialogflow
    req = request.get_json(force=True) #combierto los valores en un json
    if req.get('session'): #verifica la session
        return req.get('session') #devuelve la session
    else:
        return ''#devuelve valor nulo

def lifetime(sesion,variable,txt=""): #verifica la existencia del custom o variable global
    req = request.get_json(force=True) #combierto los valores en un json
    if req.get('queryResult').get('outputContexts'):
        partes=req.get('queryResult').get('outputContexts')
        txt="no"
        sal=sesion+"/contexts/"+variable #concatena la sesion y la ariable
        contador=0 #genera un contador
        for part in partes: #cre un ciclo
            if req.get('queryResult').get('outputContexts')[contador].get('name')==sal: #verifica el nombre de la variabele
                txt=req.get('queryResult').get('outputContexts')[contador].get('name') #retorna la variable
        contador=contador+1 #genera un contador
        return txt #retorna un valor
    else:
        return ''#retorna un valor nulo

def custom(metodo,variables,tiempodevida,parametros,numero,*destroycustom):
    metodo=metodo[:-1]
    contador=1
    variable=', "outputContexts": [ { "name": "'
    sesion=getsesion()
    variable=variable+sesion+'/contexts/'+variables+'", '
    variable=variable+'"lifespanCount": '+str(tiempodevida)
    if type(parametros)==str:
        if parametros!="":
            variable=variable+', "parameters": { "'+parametros+'":"'+numero+'", "'+parametros+'.original": "'+numero+'" } } ]}'
            variable=variable+'"} } '
        else:
            variable=variable+' } '
        
    if type(parametros)==list:
        variable=variable+', "parameters": { "'
        contar=0
        for param  in parametros:
            if contador==1:
                variable=variable+''+param+'":"'+numero[contador-1]+'", "'+param+'.original": "'+numero[contador-1]+'"'
            else:
                variable=variable+', "'+param+'":"'+numero[contador-1]+'", "'+param+'.original": "'+numero[contador-1]+'"'
            contador=contador+1
        variable=variable+'} } '
    if len(destroycustom)!=0:
        for vaciar in destroycustom:
            print("uno\n")
    variable=variable+']}'
    return metodo+variable
        




#esta sirve para regresar las variables creadas en dialogflow
    #basta con usar variable_recibir=lib.variable('nombre de variable') //si esta no existe regresa un valor nulo
def variable(nombre):
    req = request.get_json(force=True) #combierto los valores en un json
    if req.get('queryResult').get('parameters').get(nombre): #verifica si existe la variable
        return req.get('queryResult').get('parameters').get(nombre) #retorno del texto
    else:
        return '' #no regreso ningun valor
#endregion

#region obtener_recursos
    #esta funcion sirve para la tomar el texto completo enviado desde dialogflow
    #basta para recivirla poner variable_recibir=lib.texto()
def texto():
    req = request.get_json(force=True) #combierto los valores en un json
    if req.get("queryResult").get("queryText"): #verifico la existencia de algun texto
        return req.get("queryResult").get("queryText") #retorna el texto completo por si se necesita para una herramienta de analisis de sentimiento
    else:
        return '' #no regreso ningun valor
    #esta funcion sirve para tomar la url de la imagen
    #basta para recivirla variable_recivir=lib.imagen()
def imagen():
    req = request.get_json(force=True) #combierto los valores en un json
    if req.get('originalDetectIntentRequest').get('payload').get('data').get('message').get('attachments')[0].get('payload').get('url'): #analisa la url de la imagen
        return req.get('originalDetectIntentRequest').get('payload').get('data').get('message').get('attachments')[0].get('payload').get('url') #regresa el valor de la imagen
    else:
        return '' #no regreso ningun valor
def obtenertipoarchivo():
    try:
        req = request.get_json(force=True) #combierto los valores en un json
        inputtest=req.get('originalDetectIntentRequest').get('payload').get('data').get('message').get('text')
        inputtest.encode('ascii', 'ignore').decode('ascii')
        if inputtest=='':
            return ''
        else:
            if req.get('originalDetectIntentRequest').get('payload').get('data').get('message').get('attachments')[0].get('type'):
                return req.get('originalDetectIntentRequest').get('payload').get('data').get('message').get('attachments')[0].get('type')
            else:
                return ''
    
    except Exception as e:
        return ''

    return ''
#endregion
#endregion

#region envios
#region mensajes
#esta funcion envia un mensaje ha todas las plataformas
    #funcion con mensaje estatico
    # imprimir lib.msj('hola')
    #funcion para array
    #1)
    #   mensaje=[]
    #   mensaje.append('msj1')
    #   mensaje.append('msj2')
    #   mensaje.append('msj3')
    #   imprimir lib.msj(mensaje)
    #   nota tambien puede usar elementos STRING o diccionarios

def msj(text):
    if type(text)==list:
        rndtext=random.choice(text) #por medio de la libreria random toma un valor del array
        return '{"fulfillmentText": "'+rndtext+'", "fulfillmentMessages": [ { "text": { "text": [ "'+rndtext+'" ] } } ]}' #regresa el json //posibles mensajes ejemplo: msj1,msj2,msj3
    elif type(text)==dict: #verifica si es un diccionario
        rndtext=random.choice(list(text.values())) #por medio de la libreria random toma un valor del array
        return '{"fulfillmentText": "'+rndtext+'", "fulfillmentMessages": [ { "text": { "text": [ "'+rndtext+'" ] } } ]}' #regresa el json //posibles mensajes ejemplo: msj1,msj2,msj3
    else:
        return '{"fulfillmentText": "'+text+'", "fulfillmentMessages": [ { "text": { "text": [ "'+text+'" ] } } ]}' #regresa el json
#endregion
#region medias
#esta es una funcion de llamada
    #   una sola imagen
    #   imprimir lib.enviarimagenes('url imagen')
    #   variedad de imagenes  
    #   img=[]
    #   img.append('urlimg1')
    #   img.append('urlimg2')
    #   img.append('urlimg3')
    #   imprimir lib.enviarimagenes(img)
    #   nota tambien puede usar elementos STRING o diccionarios
def enviarimagenes(imagen,plataforma): 
    if type(imagen)==list: #comprueba si es un array para imprimir varias imagenes
        cadena='{"fulfillmentMessages":[' #crea una cadena de texto que ayuda al retorno del mensaje
        for img in imagen: #creo un conteo de las variables
            cadena=cadena+'{"image":{"imageUri":"'+img+'"},"platform":"'+plataforma+'"},' # concateno la url de las imagenes a la cadena
        cadena=cadena+'{"payload":{}}]}' # termino la cadena
        return cadena #regreso el valor
    elif type(imagen)==dict: #verifica si el elemento es un diccionario
        cadena='{"fulfillmentMessages":[' #crea una cadena de texto que ayuda al retorno del mensaje
        for img in imagen: #creo un conteo de las variables
            cadena=cadena+'{"image":{"imageUri":"'+img+'"},"platform":"'+plataforma+'"},' # concateno la url de las imagenes a la cadena
        cadena=cadena+'{"payload":{}}]}' # termino la cadena
        return cadena #regreso el valor
    else:
        cadena='{"fulfillmentMessages":[' #crea una cadena de texto que ayuda al retorno del mensaje
        cadena=cadena+'{"image":{"imageUri":"'+imagen+'"},"platform":"'+plataforma+'"},' # concateno la url de las imagenes a la cadena
        cadena=cadena+'{"payload":{}}]}' # termino la cadena
        return cadena #regreso el valor
# nota esta tiene el potencial de llamar a solo una imagen y el texto puede ser randomizado estatico o ninguno dado qye el texto es opcional
    #para usarlo basta con crear un array o diccionario de las imagenes tanto como el array, diccionario o texto STRING del texto
    #para llamardo basta con poner imprimir lib.rndenviarimagenes(arrayimagen,origenes) Nota esta es sin texto
    #para llamardo basta con poner imprimir lib.rndenviarimagenes(arrayimagen,origenes,texto) imprime texto estatico texto='lo que quieres'
    #para llamardo basta con poner imprimir lib.rndenviarimagenes(arrayimagen,origenes,arraytexto) arraytexto='el array o diccionario' cual sea de los tres
def rndenviarimagenes(imagen,plataforma,texto=''):
    if type(texto)==list: #comprueba si es un array para imprimir varias imagenes
         txt=random.choice(texto) #toma un valor del array random
    elif type(texto)==dict: #verifica si el elemento es un diccionario
        txt=random.choice(list(texto.values())) #toma un valor array del diccionario
    else:
        txt=texto #toma dato del STRING
    if type(imagen)==list: #comprueba si es un array para imprimir varias imagenes
        img=random.choice(imagen) #toma un valor del array random
    elif type(imagen)==dict: #verifica si el elemento es un diccionario
        img=random.choice(list(imagen.values())) #toma un valor array del diccionario
    else:
        exit() #sale del sistema
    cadena='{"fulfillmentMessages":[' #empieza la cadena
    cadena=cadena+'{"image":{"imageUri":"'+img+'"},"platform":"'+plataforma+'"},' # almacena la imagen
    cadena=cadena+'{"text": { "text": [ "'+str(txt)+'" ] },"platform":"'+plataforma+'"},' #crea el texto a no ser que no exista alguno
    cadena=cadena+'{"payload":{}}]}' #termina la cadena
    return cadena #regresa la cadena



def enviartarjetas(tarjeta,plataforma):
    cadena='{"fulfillmentMessages": [' #empieza la cadena
    
    for numero_tarjeta in tarjeta: #cuenta los valores del diccionario
        contador=1 #ayuda al contador
        cadena=cadena+'{"card": {"title": "'+tarjeta[numero_tarjeta]['titulo'] #continua la cadena
        cadena=cadena+'", "subtitle": "'+tarjeta[numero_tarjeta]['subtitulo'] #continua la cadena
        cadena=cadena+'", "imageUri": "'+tarjeta[numero_tarjeta]['img']+'"' #continua la cadena

        variable_boton=tarjeta[numero_tarjeta]['boton'] #crea un array de otro array
        for bottones in variable_boton: #crea un ciclo en las variables
            if contador==1:
                cadena=cadena+', "buttons": [ { "text": "'+bottones+'"} ' #crea los botones
            else:
                cadena=cadena+', { "text": "'+bottones+'"} ' #crea los botones
            contador=contador+1 #aumenta el contador
        cadena=cadena+']}, "platform": "'+plataforma+'"},' #crea  
    cadena=cadena+'{"payload":{}}]}' #termina la cadena
    return cadena #regresa la cadena
#
def enviarrespuestasrapidas(repuestas,plataforma):
    cadena='{ "fulfillmentMessages": [ { "quickReplies": { "title": "'+repuestas['titulo'][0]+'",  "quickReplies": [' #empieza la cadena
    botones=repuestas['boton']#
    cadena_botones=''
    for botonesinfo in botones:
        if cadena_botones=='':
            cadena_botones=cadena_botones+'"'+botonesinfo+'"'
        else:
            cadena_botones=cadena_botones+',"'+botonesinfo+'"'
    cadena=cadena+cadena_botones+']},"platform": "'+plataforma+'"},{"payload":{}}]}'
    return cadena
#endregion
#region facebook
def enviarvideofacebook(url,plataforma):
    if type(url)==dict:
        url=random.choice(list(url.values()))
    elif type(url)==list:
        url=random.choice(url)
    a='{ "fulfillmentMessages": [ { "text": { "text": [ "" ] }, "platform": "'+plataforma+'" },{ "payload": { "'+plataforma.lower()+'": { "attachment": { "payload": {'
    a=a+'"elements": ['
    a=a+' { "url": "'+url+'", "media_type": "video" } ], "template_type": "media"'
    a=a+'},"type": "template" }}},"platform": "'+plataforma+'" }]}'
    return a
            
          
    
def respuestarapidafacebook(titulo,respuestas,plataforma,img=''):
    contador=1
    cadena='{ "fulfillmentMessages": [ { "text": { "text": [ "" ] }, "platform": "'+plataforma+'" },{ "payload": { "'+plataforma.lower()+'": { "text": "'+titulo+'", "quick_replies":['
    if img=='color' or img=='colors':
        color=[]
        color.append('https://imgtoboot.000webhostapp.com/pack/azul.jpg')
        color.append('https://imgtoboot.000webhostapp.com/pack/cafe.jpg')
        color.append('https://imgtoboot.000webhostapp.com/pack/negro.jpg')
        color.append('https://imgtoboot.000webhostapp.com/pack/rojo.jpg')
        color.append('https://imgtoboot.000webhostapp.com/pack/rosa.jpg')
        if type(respuestas)==str:
            color=random.choice(color)
            cadena=cadena+'{ "content_type":"text",  "title":"'+respuestas+'",  "payload":"'+respuestas+'", "image_url":"'+color+'" }'
            return cadena+'] } },"platform": "'+plataforma+'" }]}'

        else:
            random.shuffle(color)
            contar=0
            coma=1
            numerodeelementos=len(color)-1
            for resp in respuestas:
                if coma==2:
                    cadena=cadena+', '
                cadena=cadena+'{ "content_type":"text",  "title":"'+resp+'",  "payload":"'+resp+'", "image_url":"'+color[contar]+'" }'
                contar=contar+1
                coma=2
                if contar>numerodeelementos:
                    contar=0
            return cadena+'] } },"platform": "'+plataforma+'" }]}'


    elif type(respuestas)==str:
        cadena=cadena+'{ "content_type":"text",  "title":"'+respuestas+'",  "payload":"'+respuestas+'", "image_url":"'+img+'" }'
        return cadena+'] } },"platform": "'+plataforma+'" }]}'
    elif type(respuestas)==str and type(img)==list:
        rndimg=random.choice(img.values())
        cadena=cadena+'{ "content_type":"text",  "title":"'+respuestas+'",  "payload":"'+respuestas+'", "image_url":"'+rndimg+'" }'
        return cadena+'] } },"platform": "'+plataforma+'" }]}'
    elif type(respuestas)!=str and type(respuestas)!=str:
        c=0
        if len(respuestas)==len(img):
            for respuestasasignadas in respuestas:
                if contador==2:
                    cadena=cadena+', '
                cadena=cadena+'{ "content_type":"text",  "title":"'+respuestasasignadas+'",  "payload":"'+respuestasasignadas+'", "image_url":"'+img[c]+'" }'
                contador=2
                c=c+1
            return cadena+'] } },"platform": "'+plataforma+'" }]}'
        else:
            for respuestasasignadas in respuestas:
                rndimg=random.choice(img)
                if contador==2:
                    cadena=cadena+', '
                cadena=cadena+'{ "content_type":"text",  "title":"'+respuestasasignadas+'",  "payload":"'+respuestasasignadas+'", "image_url":"'+rndimg+'" }'
                contador=2
                c=c+1
            return cadena+'] } },"platform": "'+plataforma+'" }]}'
    else:
        for respuestasasignadas in respuestas:
            if contador==2:
                cadena=cadena+', '
            cadena=cadena+'{ "content_type":"text",  "title":"'+respuestasasignadas+'",  "payload":"'+respuestasasignadas+'", "image_url":"'+img+'" }'
            contador=2
        return cadena+'] } },"platform": "'+plataforma+'" }]}'
    
def enviarurlfacebook(titulo,plataforma,url):
    c=1
    a= '{ "fulfillmentMessages": [ { "text": { "text": [ "" ] }, "platform": "'+plataforma+'" },{ "payload": { "'+plataforma.lower()+'": { "attachment": { "payload": {'
    a=a+' "template_type": "button", "text": "'+titulo+'", "buttons": ['
    for urlfor in url:
        if c==2:
            a=a+', '
        a=a+'{"title": "'+url[urlfor][0]+'", "type": "web_url", "url": "'+url[urlfor][1]+'"}'
        c=2
    a=a+']},"type": "template" }}},"platform": "'+plataforma+'" }]}'
    return a
#endregion
#region payload
def enviarpdf_audio_video(url,plataforma,tipoarchivo,texto=''):
    if type(texto)==list:
        text=random.choice(texto)
    elif type(texto)==dict:
        text=random.choice(list(texto.values()))
    else:
        text=texto
    if(tipoarchivo=="audio"):
        return enviaraudio(url,plataforma,text)
    elif(tipoarchivo=="video"):
        return enviarvideo(url,plataforma,text)
    elif(tipoarchivo=="document"):
        return enviarpdf(url,plataforma,text)
    else:
        return msj('Error decide un tipo de archivo de audio, video, document')

def variablerandom(*vari):
    variablerandom=random.choice(vari)
    return variablerandom

def enviarpdf(url,plataforma,texto=''):
    return '{ "fulfillmentMessages": [ { "text": { "text": [ "'+texto+'" ] }, "platform": "'+plataforma+'" },{ "payload": { "'+plataforma.lower()+'": { "attachment": { "payload": { "url": "'+url+'" },"type": "file" }}},"platform": "'+plataforma+'" }]}'

def enviaraudio(url,plataforma,texto=''):
    return '{ "fulfillmentMessages": [ { "text": { "text": [ "'+texto+'" ] }, "platform": "'+plataforma+'" },{ "payload": { "'+plataforma.lower()+'": { "attachment": { "payload": { "url": "'+url+'" },"type": "audio" }}},"platform": "'+plataforma+'" }]}'
def enviarvideo(url,plataforma,texto=''):
    return '{ "fulfillmentMessages": [ { "text": { "text": [ "'+texto+'" ] }, "platform": "'+plataforma+'" },{ "payload": { "'+plataforma.lower()+'": { "attachment": { "payload": { "url": "'+url+'" },"type": "video" }}},"platform": "'+plataforma+'" }]}'
#endregion
#endregion