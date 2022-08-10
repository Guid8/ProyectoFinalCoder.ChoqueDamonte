from django import http
from django.shortcuts import render
from AppCoder.models import Socios, Nosotros, Instalaciones
from django.http import HttpResponse
from AppCoder.forms import SociosForm
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




def inicio(request):
    return render(request, "AppCoder/inicio.html")  

def instalaciones(request):
    return render(request, "AppCoder/instalaciones.html")   

def nosotros(request):
    return render(request, "AppCoder/nosotros.html")     

def socioFormulario(request):


    if request.method=="POST":
        form= SociosForm(request.POST)
        print(form)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre= info["nombre"]
            apellido= info["apellido"]
            socios= Socios(nombre=nombre, apellido=apellido)
            socios.save()
            return render (request, "AppCoder/inicio.html")
    else:
        form= SociosForm()        
    return render (request, "AppCoder/socioFormulario.html", {"form":form})


def sociosFormulario(request):
    if (request.method== "POST"):
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
    return render (request, "AppCoder/socioForm.html", {"form":form})

def eliminarSocio(request, nombre_socio):
    socios= Socios.objects.get(nombre=nombre_socio)
    socios.delete()

    socios= Socios.objects.all()
    return render(request, "AppCoder/leerSocios.html", {"socios":socios})

def busquedaSocios(request):
    return render (request, "AppCoder/busquedaSocios.html")



def buscar(request):
    if request.GET["apellido"]:
        apellido= request.GET["apellido"]
        socios= socios.objects.filter(apellido=apellido)
        return render(request, "AppCoder/resultadosBusqueda.html", {"socios":socios})
    else:
        return render(request, "AppCoder/busquedaSocios.html", {"error":"no se ingreso ninguna comision"})    


def leerSocios(request):
    socios= Socios.objects.all()
    return render(request, "AppCoder/leerSocios.html", {"socios":socios})

def editarSocio(request, nombre_socio):
    socios= Socios.objects.get(nombre=nombre_socio)
    if request.method=="POST":
        form= SociosForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            socios.nombre= info["nombre"]
            socios.apellido= info["apellido"]
            socios.email= info["email"]
            socios.actividad= info["actividad"]
            socios.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form= SociosForm(initial={"nombre":socios.nombre, "apellido":socios.apellido,
        "email":socios.email, "profesion":socios.actividad})

    return render(request, "AppCoder/editarSocio.html", {"formulario":form,
    "nombre_socio":nombre_socio})


class sociosList(ListView):
    model=Socios
    template_name= "AppCoder/SociosList.html"

class sociosDetalle(DetailView):
    model=Socios
    template_name="Appcoder/socios_detalle.html"

class sociosUpdate(UpdateView):
    model = Socios
    success_url = reverse_lazy('socios_listar')
    fields= ['nombre','apellido','email']  


class sociosCreacion(CreateView):
    model = Socios
    success_url = reverse_lazy('socios_listar')
    fields= ['nombre','apellido','email']

class sociosDelete(DeleteView):
    model = Socios
    success_url = reverse_lazy('socios_listar')