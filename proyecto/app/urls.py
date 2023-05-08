from django.urls import path
from app import views
from app.views import listar_alumnos, listar_materias, listar_profesores

urlpatterns = [
    path('materias/', listar_materias, name="materias"),
    path('alumnos/', listar_alumnos, name="alumnos"),
    path('profesores/', listar_profesores, name="profesores")
]
