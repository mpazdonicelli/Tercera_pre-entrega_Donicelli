from django.urls import path
from app import views
from proyecto.views import saludar

urlpatterns = [
    path('saludo/', saludar),
]
