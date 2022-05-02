from django.urls import path
from .views import *

urlpatterns = [
    path('', list_familiar),
    path('crear', create_familiar, name='create_familiar'),
]