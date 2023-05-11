from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Materia, Alumno, Profesor
from app.forms import MateriaFormulario, AlumnoFormulario, ProfesorFormulario
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

def crear_materia(request):
    if request.method == "POST":
        formulario = MateriaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data 
            nombre = data["nombre"]
            año = data["año"]
            materia = Materia(nombre=nombre, año=año) 
            materia.save()

            url_exitosa = reverse('listar_materias') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = MateriaFormulario()
    http_response = render(
        request=request,
        template_name='crear_materia.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_materia(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        materias = Materia.objects.filter(nombre__contains=busqueda)
        contexto = {
            "materias": materias,
        }
        http_response = render(
            request=request,
            template_name='app/materias.html',
            context=contexto,
        )
        return http_response