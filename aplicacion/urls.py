from django.urls import path
from .views import *

urlpatterns = [
    path('list_familiar', list_familiar),
    path('familiar', familiar, name='familiar'),
    path('list_estudiante', list_estudiante),
    path('list_materia', list_materia),
    path('materia', materia, name='materia'),
    path('estudiante', estudiante, name='estudiante'),
    path('busqueda', busqueda),
    path('buscar', buscar),
    path('', inicio),
]