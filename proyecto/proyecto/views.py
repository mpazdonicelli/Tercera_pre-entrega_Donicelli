from django.http import HttpResponse


def saludar(request):
    return HttpResponse ("Bienvenido/a")