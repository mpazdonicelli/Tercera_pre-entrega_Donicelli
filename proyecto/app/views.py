from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Materia, Alumno, Profesor

# Create your views here.

def listar_materias(request):
    contexto = {
        "materias": Materia.objects.all(),
    }
    http_response= render(
        request=request,
        template_name='app/materias.html',
        context=contexto,
    )
    return http_response

def listar_alumnos(request):
    contexto = {
        "alumnos": Alumno.objects.all(),
    }
    http_response= render(
        request=request,
        template_name='app/alumnos.html',
        context=contexto,
    )
    return http_response

def listar_profesores(request):
    contexto = {
        "profesores": Profesor.objects.all(),
    }
    http_response= render(
        request=request,
        template_name='app/profesores.html',
        context=contexto,
    )
    return http_response
