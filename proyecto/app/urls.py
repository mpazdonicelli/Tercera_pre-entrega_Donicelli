from django.urls import path
from app import views
from proyecto.views import saludar
from app.views import inicio, materias, alumnos, profesores

urlpatterns = [
    path('saludo/', saludar),
    path('inicio/', inicio, name="inicio"),
    path('materias/', materias, name="materias"),
    path('alumnos/', alumnos, name="alumnos"),
    path('profesores/', profesores, name="profesores")
]
