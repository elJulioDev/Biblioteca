from django.db import models
from django.contrib.auth.models import AbstractUser

# Esta clase de aqui sirve para crear una tabla para los autores y almacenarlos
class Autor(models.Model):
    Nombre_Aut = models.TextField(max_length=255)
    def __str__(self):
        return str(self.Nombre_Aut)

# Esta clase de aqui sirve para crear una tabla para los categorias y almacenarlos
class Categoria(models.Model):
    Nombre_Cat = models.TextField(max_length=255)
    def __str__(self):
        return str(self.Nombre_Cat)

# Esta clase de aqui sirve para crear una tabla para los editoriales y almacenarlos
class Editorial(models.Model):
    Nombre_Edi = models.TextField(max_length=255)
    def __str__(self):
        return str(self.Nombre_Edi)

# Esta clase de aqui sirve para crear una tabla para los libros y almacenarlos
class Libro(models.Model):
    Titulo = models.TextField(max_length=255)
    Num_Ser = models.IntegerField(null=False)
    Publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Titulo) + "-" + str(self.Num_Ser)+ "-" + str(self.Publicacion)+ "-" + str(self.autor)+ "-" + str(self.categoria)+ "-" + str(self.editorial)

# Esta clase de aqui sirve para crear una tabla para los usuarios y
# almacenarlos con sus respectivas contraseñas y datos
class Usuario(models.Model):
    rut = models.TextField(max_length=255, unique=True)
    nombre = models.TextField(max_length=255)
    ape_pat = models.TextField(max_length=255)
    ape_mat = models.TextField(max_length=255)
    direccion = models.TextField(max_length=255)
    telefono = models.IntegerField(null=False)
    correo = models.TextField(max_length=255)
    nacimiento = models.DateField()
    contraseña = models.TextField(max_length=255)
    def __str__(self):
        return str(self.rut) + "-" + str(self.nombre) + "-" + str(self.ape_pat) + "-" + str(self.ape_mat) + "-" + str(self.direccion) + "-" + str(self.telefono) + "-" + str(self.correo) + "-" + str(self.nacimiento)+ "-" + str(self.contraseña)

# Esta clase de aqui sirve para crear una tabla para los prestamos de los usuarios
# y los deja almacenados
class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.usuario.nombre) + "-" + str(self.libro.Titulo)