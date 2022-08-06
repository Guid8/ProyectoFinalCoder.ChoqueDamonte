from django import http
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.views.generic import ListView



def inicio(request):
    return render(request, "AppCoder/inicio.html")  

def perfil(request):
    return render(request, "AppCoder/perfil.html")  

def socios(request):
    return render(request, "AppCoder/socios.html")  

def instalaciones(request):
    return render(request, "AppCoder/instalaciones.html")   

def nosotros(request):
    return render(request, "AppCoder/nosotros.html")     

def perfilFormulario(request):


    if request.method=="POST":
        form= PerfilForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido= info["apellido"]
            perfil= Perfil(nombre=nombre, apellido=apellido)
            perfil.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= PerfilForm()        
    return render (request, "AppCoder/perfilFormulario.html", {"formulario":form})


def sociosFormulario(request):
    if request.method== "POST":
        form= SociosForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            actividad= info["actividad"]
            socios=Socios(nombre=nombre, apellido=apellido, email=email, actividad=actividad)
            socios.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= SociosForm()  
    return render (request, "AppCoder/profeForm.html", {"formulario":form})
  
def eliminarSocio(request, nombre_profesor):
    socios= Socios.objects.get(nombre=nombre_profesor)
    socios.delete()

    socios= Socios.objects.all()
    return render(request, "AppCoder/leerSocios.html", {"socios":socios})
   

def busquedaComision(request):
    return render (request, "AppCoder/busquedaComision.html")

def __str__(self):
    return f"nombre: {self.nombre} - Apellido{self.apellido} - E-Mail {self.email} - Profesion {self.profesion}" 

def buscar(request):
    if request.GET["comision"]:
        comi= request.GET["comision"]
        perfil= perfil.objects.filter(comision=comi)
        return render(request, "AppCoder/resultadosBusqueda.html", {"perfil":perfil})
        return render(request, "AppCoder/busquedaComision.html", {"error":"no se ingreso ninguna comision"})    
        

def leerSocios(request):
    socios= socios.objects.all()
    return render(request, "AppCoder/leerSocios.html", {"socios":socios})

def editarSocios(request, nombre_profesor):
    socios=Socios.objects.get(nombre=nombre_profesor)
    if request.method=="POST":
        form= SociosForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            socios.nombre=info ["nombre"]
            socios.apellido=info ["apellido"]
            socios.email= info ["email"]
            socios.actividad= info["actividad"]
            socios.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form= SociosForm(initial={"nombre":socios.nombre, "apellido":socios.apellido,
        "email":socios.email, "profesion":socios.profesion})

    return render(request, "AppCoder/editarSocio.html", {"formulario":form,
    "nombre_socio":nombre_profesor})

