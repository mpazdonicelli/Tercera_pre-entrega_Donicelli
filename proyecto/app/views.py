from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "app/index.html")

def materias(request):
    return render(request, "app/materias.html")

def alumnos(request):
    return render(request, "app/alumnos.html")

def profesores(request):
    return render(request, "app/profesores.html")