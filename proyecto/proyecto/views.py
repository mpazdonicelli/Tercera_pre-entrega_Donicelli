from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse ("Bienvenido/a")

def inicio(request):
    contexto = {}
    http_response= render(
        request=request,
        template_name='app/index.html',
        context=contexto,
    )
    return http_response