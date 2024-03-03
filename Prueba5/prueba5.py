"""
    Parametros:
        correos (list): Lista de correos electrónicos como objeto Lista
        asunto (string): Asunto del correo como cadena de texto
        rutas_adjuntos (list): Lista de rutas de archivos a adjuntar como una Lista
        cuerpo_correo (string): Cuerpo del correo como cadena de texto

    Otras variables:
        ValueError: Manejador de errores que almacena 
        una cadena de texto en caso de que se cumpla 
        un evento.
        En este caso si se intentan adjuntar más de cinco archivos.
"""
    
from typing import List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

def enviar_correos(correos: List[str], asunto: str, rutas_adjuntos: List[str], cuerpo_correo: str) -> None:
   
     # Verificar si hay más de cinco archivos adjuntos
    if len(rutas_adjuntos) > 5:
        raise ValueError("Se deben adjuntar como máximo cinco archivos.")

    #Creando mensaje multipart. 
    #Libreria que nos permite construir un correo sin formato 
    mensaje = MIMEMultipart()
    mensaje['From'] = 'jcamiloif.ji@gmail.com'  # Reemplaza con tu dirección de correo
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo_correo, 'plain'))

    #Agregando destinatarios
    mensaje['To'] = correos[0] #Envio directo al primer correo de la lista
    mensaje['Cc'] = ','.join(correos[1:]) if len(correos) > 1 else '' #Envio como copia al resto de correos de la lista, en caso de que haya mas de un destinatario

    #Adjuntar archivos
    for ruta_adjunto in rutas_adjuntos:
        adjunto = MIMEApplication(open(ruta_adjunto, 'rb').read())
        adjunto.add_header('Content-Disposition', 'attachment', filename=ruta_adjunto.split('/')[-1])
        mensaje.attach(adjunto)

    #Establece conexión con el servidor SMTP y enviar correo
    with smtplib.SMTP('smtp.gmail.com', 587) as servidor_smtp:
        servidor_smtp.starttls()
        servidor_smtp.login('jcamiloif.ji@gmail.com', 'nmtq rrun thkd oisd ') 
        servidor_smtp.send_message(mensaje)




try:
    enviar_correos(['juan-iguaran@hotmail.com', 'jciguaranf@eafit.edu.co', 'jcamiloif.ji@gmail.com'],
                   'Asunto del correo',
                   ['archivo1.pdf', 'archivo2.doc', 'archivo3.doc', 
                    'archivo4.doc', 'archivo5.pdf', 'archivo6.pdf'],
                   'Cuerpo del correo.')
    print("Correo enviado exitosamente.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error al enviar el correo: {e}")