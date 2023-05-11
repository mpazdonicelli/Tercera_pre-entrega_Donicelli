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
    
def agregar_alumno(request):
    if request.method == "POST":
        formulario = AlumnoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data 
            nombre = data["nombre"]
            apellido = data["apellido"]
            alumno = Alumno(nombre=nombre, apellido=apellido) 
            alumno.save()

            url_exitosa = reverse('listar_alumnos') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = AlumnoFormulario()
    http_response = render(
        request=request,
        template_name='agregar_alumno.html',
        context={'formulario': formulario}
    )
    return http_response

def agregar_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data 
            nombre = data["nombre"]
            apellido = data["apellido"]
            profesor = Profesor(nombre=nombre, apellido=apellido) 
            profesor.save()

            url_exitosa = reverse('listar_profesor') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    http_response = render(
        request=request,
        template_name='agregar_profesor.html',
        context={'formulario': formulario}
    )
    return http_response