from django.db import models



class Socios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    actividad=models.CharField(max_length=50)
        
    def __str__(self):

        return f"nombre: {self.nombre} - apellido{self.apellido} - email {self.email} - actividad {self.actividad}"


class Instalaciones(models.Model):
    nombre=models.CharField(max_length=50)
    texto=models.CharField(max_length=150)
    

class Nosotros(models.Model):
    texto=models.CharField(max_length=150)


