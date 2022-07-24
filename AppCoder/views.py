from django import http
from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse
from AppCoder.forms import CursoForm, ProfeForm

def curso(self):
    curso = Curso(nombre="Django", comision=96)
    curso.save()
    texto=f"Curso creado: {curso.nombre},{curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")  

def cursos(request):
    return render(request, "AppCoder/cursos.html")  

def profesores(request):
    return render(request, "AppCoder/profesores.html")  

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")   

def entregables(request):
    return render(request, "AppCoder/entregables.html")     

def cursoFormulario(request):


    if request.method=="POST":
        form= CursoForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            comision= info["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= CursoForm()        
    return render (request, "Appcoder/cursoFormulario.html", {"formulario":form})



def profeFormulario(request):
    if request.method== "POST":
        form= ProfeForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= ProfeForm()  
    return render (request, "Appcoder/profeForm.html", {"formulario":form})

def busquedaComision(request):
    return render (request, "AppCoder/busquedaComision.html")


def buscar(request):
    comision=request.GET.get("comision")
    respuesta= f"estoy buscando la comision : {comision}"
    return HttpResponse(respuesta)
        