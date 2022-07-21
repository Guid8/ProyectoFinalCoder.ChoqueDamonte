from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

def curso(self):
    curso = Curso(nombre="Django", comision=96)
    curso.save()
    texto=f"Curso creado: {curso.nombre},{curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request, "Appcoder/inicio.html")

def cursos(request):
    return render(request, "Appcoder/cursos.html")

def profesores(request):
    return render(request, "Appcoder/profesores.html")

def estudiantes(request):
    return render(request, "Appcoder/estudiantes.html")

def entregables(request):
    return render(request, "Appcoder/entregables.html")

def cursoFormulario(request):
    return render(request, "AppCoder/cursoFormulario.html")


    