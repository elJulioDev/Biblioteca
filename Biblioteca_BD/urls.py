from django.contrib import admin
from django.urls import path
from Biblioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.iniciar_sesion, name='inicio_sesion'),
    path('inicio_sesion', views.iniciar_sesion, name='inicio_sesion'),
    path('index_admin/', views.mostrarIndexAdmin, name='index_admin'),
    path('index/', views.mostrarIndexUsuario, name='index'),
    path('registrarse', views.mostrarRegistroUsuario),
    path('verperfil', views.MostrarPerfil, name='ver_perfil'),
    path('verperfiladmin', views.MostrarPerfilAdmin, name='ver_perfiladmin'),
    path('RegistrarAutor', views.mostrarFormRegistroAutor, name="form_registrarAutor"),
    path('RegistrarCategoria', views.mostrarFormRegistroCategoria, name="form_registrarCategoria"),
    path('RegistrarEditorial', views.mostrarFormRegistroEditorial, name="form_registrarEditorial"),
    path('registrar_Usuario', views.mostrarRegistroUsuarioAdmin, name='registrarUsuario'),
    path('mostrar_prestamos/', views.mostrarPrestamos, name="mostrar_prestamos"),
    path('mostrar_prestamosAdmin/', views.mostrarPrestamosAdmin, name="mostrar_prestamosAdmin"),
    path('eliminar_prestamo/<int:id>', views.eliminarPrestamo, name='eliminar_prestamo'),
    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
    path('registrar_libro',views.mostrarFormRegistrarLibro,name='registrarLibro'),
    path('modificar_libro/<int:libro_id>/', views.mostrarFormModificarLibro, name='modificar_libro'),
]