from django import forms

class familiarformulario(forms.Form):
    nombre= forms.CharField()
    parentezco=forms.CharField()
    edad=forms.IntegerField()
    fecha_nacimiento=forms.DateField()
    ocupacion=forms.CharField()


class estudianteformulario(forms.Form):
    nombre= forms.CharField()
    carrera=forms.CharField()
    edad=forms.IntegerField()
    fecha_nacimiento=forms.DateField()

class materiaformulario(forms.Form):
    nombre= forms.CharField()
    area=forms.CharField()
    creditos=forms.IntegerField()
    



