from django.db import models

class Perfil(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.IntegerField()
    fechaDeNacimiento=models.DateField()
    email=models.EmailField()
    numeroDeSocio=models.IntegerField()

    
    def __str__(self):
        return self.nombre+" "+str(self.apellido)

class Socios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    numeroDeSocio=models.IntegerField()
    actividad=models.CharField(max_length=50)

class Instalaciones(models.Model):
    nombre=models.CharField(max_length=50)
    texto=models.CharField(max_length=150)
    

class Nosotros(models.Model):
    texto=models.CharField(max_length=150)


