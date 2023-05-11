from django.urls import path
from app import views
from app.views import listar_alumnos, listar_materias, listar_profesores, crear_materia, buscar_materia, agregar_alumno, agregar_profesor
from app.forms import MateriaFormulario, ProfesorFormulario, AlumnoFormulario

urlpatterns = [
    path('materias/', listar_materias, name="materias"),
    path('alumnos/', listar_alumnos, name="alumnos"),
    path('profesores/', listar_profesores, name="profesores"),
    path('crear-materia/', views.crear_materia, name="crear_materia"),
    path('buscar-materia/', views.buscar_materia, name="buscar_materia"),
    path('agregar-alumno/', agregar_alumno, name="agregar_alumno"),
    path('agregar-profesor/', agregar_profesor, name="agregar_profesor")
]
