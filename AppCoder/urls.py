from django.urls import path
from AppCoder.views import canchaGolf, avatares, instalaciones, nosotros, inicio, socioFormulario, busquedaSocios, buscar, leerSocios, eliminarSocio, editarSocio, sociosList, sociosDetalle, sociosCreacion, sociosUpdate, sociosDelete, login_request, register, editarPerfil, agregarAvatar
from django.contrib.auth.views import LogoutView








urlpatterns = [
    path('instalaciones/', instalaciones, name='instalaciones'),
    path('nosotros/', nosotros, name='nosotros'),
    path('', inicio, name='inicio'),
    path('socioFormulario/', socioFormulario, name='socioFormulario'),
    path('busquedaSocios/', busquedaSocios, name='busquedaSocios'),
    path('buscar/', buscar, name='buscar'),
    path('leerSocios/', leerSocios, name='leerSocios'),
    path('eliminarSocio/<nombre_socio>', eliminarSocio, name='eliminarSocio'),
    path('editarSocio/<nombre_socio>', editarSocio, name='editarSocio'),
    path('canchaGolf/', canchaGolf, name='canchaGolf'),
    path('avatares/', avatares, name='avatares'),


    path('socios/list', sociosList.as_view(), name='socios_listar'),
    path('socios/<pk>', sociosDetalle.as_view(), name='socios_detalle'),
    path('socios/nuevo/', sociosCreacion.as_view(), name='socios_crear'),
    path('socios/editar/<pk>', sociosUpdate.as_view(), name='socios_editar'),   
    path('socios/borrar/<pk>', sociosDelete.as_view(), name='socios_borrar'), 


    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
]

