from django.http import HttpResponse 
from django.template import Template, context 

def template(self):
    nombre=nombre
    edad=edad
    ocupación=ocupación
    parentezco=parentezco

    diccionario={"nombre":nombre,"edad":edad, "ocupacion":ocupación,"parentezco":parentezco}
    miarchivo=open("/Users/agus/Desktop/MVT Agustina/proyecto1/proyecto1/plantillas")
    plantilla= template(miarchivo.read())
    miarchivo.close 
