from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Familiar, Materia, Estudiante
from .forms import familiarformulario, estudianteformulario, materiaformulario

def list_familiar(request):
    familiar= Familiar.objects.all()
    context= {'familiar':familiar}
    return render(request,"familiar.html" ,context)

    
def list_estudiante(request):
    estudiante= Estudiante.objects.all()
    context= {'estudiante': estudiante}
    return render(request, "estudiante.html" ,context)


def list_materia(request):
    materia= Materia.objects.all()
    context= {'materia': materia}
    return render(request,"materia.html" ,context)


def busqueda(request):
    return render(request, "aplicacion/busqueda.html")

def buscar(request):
        if request.GET["nombre"]:
            nombre=request.GET['nombre']
            materia= Materia.objects.filter(nombre__icontains=nombre)

            return render(request, "aplicacion/busqueda.html", {"nombre": materia})
        else:
            respuesta="No enviaste datos"

        return (HttpResponse(respuesta))

def estudiante(request):
    if request.method == 'POST':
        formulario=estudianteformulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            estudiante= Estudiante(nombre=informacion['nombre'], edad=informacion['edad'], carrera=informacion['carrera'], fecha_nacimiento=informacion['fecha_nacimiento'])
            estudiante.save()
            return render(request, "aplicacion/padre.html")
    else:
        formulario=estudianteformulario()
        return render(request, "aplicacion/estudiante.html", {'formulario':formulario})

def familiar(request):
    if request.method == 'POST':
        formulario=familiarformulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            familiar= Familiar(nombre=informacion['nombre'], parentezco=informacion['parentezco'], edad=informacion['edad'], fecha_nacimiento=informacion['fecha_nacimiento'], ocupacion=informacion['ocupacion'])
            familiar.save()
            return render(request, "aplicacion/padre.html")
    else:
        formulario=familiarformulario()
        return render(request, "aplicacion/familiar.html", {'formulario':formulario})

def materia(request):
    if request.method == 'POST':
        formulario= materiaformulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            materia= Materia(nombre=informacion['nombre'], area=informacion['area'], creditos=informacion['creditos'])
            materia.save()
            return render(request, "aplicacion/padre.html")
    else:
        formulario=materiaformulario()
        return render(request, "aplicacion/materia.html", {'formulario':formulario})

    

def inicio(request):
    return render(request, 'aplicacion/padre.html')
