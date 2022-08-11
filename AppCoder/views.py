from django import http
from django.shortcuts import render
from AppCoder.models import Socios, Nosotros, Instalaciones, Avatar
from django.http import HttpResponse
from AppCoder.forms import SociosForm, UserRegisterForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def avatares(request):
    imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    return render(request, "AppCoder/avatares.html", {"imagen":imagen}) 

def canchaGolf(request):
    return render(request, "AppCoder/canchaGolf.html")  



def inicio(request):
    return render(request, "AppCoder/inicio.html")  

def instalaciones(request):
    return render(request, "AppCoder/instalaciones.html")   

def nosotros(request):
    return render(request, "AppCoder/nosotros.html")

@login_required
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

@login_required
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
@login_required
def eliminarSocio(request, nombre_socio):
    socios= Socios.objects.get(nombre=nombre_socio)
    socios.delete()

    socios= Socios.objects.all()
    return render(request, "AppCoder/leerSocios.html", {"socios":socios})

@login_required
def busquedaSocios(request):
    return render (request, "AppCoder/busquedaSocios.html")


@login_required
def buscar(request):
    if request.GET["apellido"]:
        apellido= request.GET["apellido"]
        socios= socios.objects.filter(apellido=apellido)
        return render(request, "AppCoder/resultadosBusqueda.html", {"socios":socios})
    else:
        return render(request, "AppCoder/busquedaSocios.html", {"error":"no se ingreso ninguna comision"})    

@login_required
def leerSocios(request):
    socios= Socios.objects.all()
    return render(request, "AppCoder/leerSocios.html", {"socios":socios})

@login_required
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


class sociosList(ListView, LoginRequiredMixin):
    model=Socios
    template_name= "AppCoder/SociosList.html"

class sociosDetalle(DetailView, LoginRequiredMixin):
    model=Socios
    template_name="Appcoder/socios_detalle.html"

class sociosUpdate(UpdateView, LoginRequiredMixin):
    model = Socios
    success_url = reverse_lazy('socios_listar')
    fields= ['nombre','apellido','email']  


class sociosCreacion(CreateView, LoginRequiredMixin):
    model = Socios
    success_url = reverse_lazy('socios_listar')
    fields= ['nombre','apellido','email']

class sociosDelete(DeleteView, LoginRequiredMixin):
    model = Socios
    success_url = reverse_lazy('socios_listar')


def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            usu= request.POST['username']
            clave= request.POST['password']

            usuario = authenticate(username=usu, password=clave)
            print(usuario)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppCoder/inicio.html', {'form':form,'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'AppCoder/login.html', {'form':form, 'mensaje':'usuario o clave incorrectos'})
                
        else:
            return render(request, 'AppCoder/login.html', {'form':form, 'mensaje':'FORMULARIO INVALIDO'})
    
    else:
        form = AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'form':form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                username = form.cleaned_data["username"]

                form.save()
                return render(request, 'AppCoder/inicio.html', {'form':form,'mensaje':f"Usuario Creado : {username}"})

    else:
        form = UserRegisterForm()
    return render(request, 'AppCoder/register.html', {'form': form})


@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
                info = form.cleaned_data
                usuario.email=info['email']
                usuario.password1=info['password1']
                usuario.password2=info['password2']
                usuario.save()
                return render(request, 'AppCoder/inicio.html', {'usuario':usuario,'mensaje':'USUARIO EDITADO EXITOSAMENTE!'})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'AppCoder/editarPerfil.html', {'form': form, 'usuario':usuario.username})


def agregarAvatar(request):
    if request.method=="POST":
        form= AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.get(user=request.user)
            if (avatarViejo.imagen):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=form.cleaned_data['imagen']) 
            avatar.save()
            return render(request, 'AppCoder/inicio.html', {'usuario':request.user,'mensaje':'AVATAR EXITOSAMENTE!'})
    else:
        form=AvatarForm()
    return render(request, 'AppCoder/agregarAvatar.html', {'form': form, 'usuario':request.user})





