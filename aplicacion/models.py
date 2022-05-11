
from django.db import models
from datetime import datetime

class Familiar(models.Model):
    nombre=models.CharField(max_length=50)
    parentezco=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()
    ocupacion=models.CharField(max_length=50)

class Materia(models.Model):
    nombre=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
    creditos=models.IntegerField()
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    carrera=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()

def __str__(self): 
  return f'{self.nombre}'
