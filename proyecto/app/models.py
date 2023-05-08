from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre=models.CharField(max_length=50)
    año=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} | {self.año}"
class Alumno(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} | {self.apellido}"


class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} | {self.apellido}"