from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre=models.CharField(max_length=50)
    año=models.IntegerField()

class Alumno(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()


class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()