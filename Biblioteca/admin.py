from django.contrib import admin
from Biblioteca.models import Autor, Categoria, Editorial, Libro, Usuario, Prestamo


# Con esta clase se crea un apartado con los datos de los models
# para poder registrar a los autores desde el panel de admin.
class AutorAdmin(admin.ModelAdmin):
    list_display = ['id','Nombre_Aut']

# Con esta clase se crea un apartado con los datos de los models
# para poder registrar a las categorias desde el panel de admin.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','Nombre_Cat']

# Con esta clase se crea un apartado con los datos de los models
# para poder registrar a las editoriales desde el panel de admin.
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['id','Nombre_Edi']

# Con esta clase se crea un apartado con los datos de los models
# para poder registrar los libros desde el panel de admin.
class LibroAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'Titulo',
        'Num_Ser',
        'Publicacion',
        'autor',
        'categoria',
        'editorial'
    ]

# Con esta clase se crea un apartado con los datos de los models
# para poder registrar a los usuarios desde el panel de admin.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'rut',
        'nombre',
        'ape_pat',
        'ape_mat',
        'direccion',
        'telefono',
        'correo',
        'nacimiento',
        'contraseña'
    ]

# Con esta clase se crea un apartado con los datos de los models
# para poder registrar a prestamos desde el panel de admin.
class PrestamoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'libro'
    ]
    
# Registrando las clases de administración personalizadas con los modelos correspondientes
admin.site.register(Autor,AutorAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Editorial,EditorialAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Prestamo,PrestamoAdmin)
