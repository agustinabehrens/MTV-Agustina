from django.shortcuts import render, redirect
from .models import Familiar

def list_familiar(request):
    familiar= Familiar.objects.all()
    context= {'familiar':familiar}
    return render(request,'index.html',context)

def create_familiar(request):
    nombre= request.POST["nombre"]
    parentezco= request.POST["parentezco"]
    edad= request.POST["edad"]
    fecha_nacimiento= request.POST["fecha_nacimiento"]
    ocupacion= request.POST["ocupacion"]
    familiar= Familiar(nombre=nombre, parentezco=parentezco, edad=edad, fecha_nacimiento=fecha_nacimiento, ocupacion=ocupacion)
    familiar.save()
    return redirect('/familiar')
    
