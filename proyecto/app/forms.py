from django import forms


class MateriaFormulario(forms.Form):
    nombre = forms.CharField()
    año = forms.IntegerField()

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
