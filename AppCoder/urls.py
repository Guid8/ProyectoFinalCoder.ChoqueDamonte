from django.urls import path
from .views import *


urlpatterns = [
    path('perfil/', perfil, name='perfil'),
    path('socios/', socios, name='socios'),
    path('instalaciones/', instalaciones, name='instalaciones'),
    path('nosotros/', nosotros, name='nosotros'),
    path('socios/', socios, name='socios'),
    path('', inicio, name='inicio'),
    path('perfilFormulario/', perfilFormulario, name='perfilFormulario'),
    path('sociosFormulario/', sociosFormulario, name='sociosFormulario'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar, name='buscar'),
    path('leerSocios/', leerSocios, name='leersocios'),
    path('eliminarSocio/<nombre_socios>', eliminarSocio, name='eliminarSocio'),
    path('editarSocios/<nombre_socios>', editarSocios, name='editarSocios'),
]
