from email.quoprimime import body_check
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Socios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    actividad=models.CharField(max_length=50)
        
    def __str__(self):

        return f"nombre: {self.nombre} - apellido{self.apellido} - email {self.email} - actividad {self.actividad}"


class Instalaciones(models.Model):
    nombre=models.CharField(max_length=50)
    body=RichTextField(blank=True, null=True)
    

class Nosotros(models.Model):
    body=RichTextField(blank=True, null=True)

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)


