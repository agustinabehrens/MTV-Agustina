
from django.db import models
from datetime import datetime

class Familiar(models.Model):
    nombre=models.CharField(max_length=50)
    parentezco=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateField()
    ocupacion=models.CharField(max_length=50)

def __str__(self): 
  return f'{self.nombre}'
