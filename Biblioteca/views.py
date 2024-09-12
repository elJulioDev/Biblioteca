from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Usuario, Libro, Autor, Categoria, Editorial, Prestamo
#from django.contrib.auth.hashers import make_password

# Muestra el la pagina para que los usuarios inicien sesion
def mostrarInicioSesion(request):
    return render(request, "iniciar_sesion.html")

# Muestra el index del admin donde carga todos los libros de la base de datos
def mostrarIndexAdmin(request):
    img = "libro.png"
    libros = Libro.objects.all()        
    search_term = request.GET.get('search', '')

    if search_term:
        libros = libros.filter(Titulo__icontains=search_term)

    datos = {'libros': libros, 'imagen': img, 'search_term': search_term}
    return render(request, "index_admin.html", datos)

# Muestra el index del usuario donde carga todos los libros de la base de datos
# ademas de agregar la opcion de prestamo donde al solicitar se guarda en la base de datos.
def mostrarIndexUsuario(request):
    if request.method == 'POST':
        libro_id = request.POST.get('libro_id')
        user = Usuario.objects.get(nombre=request.session['username'])
        libro = Libro.objects.get(id=libro_id)

        # Crea una instancia de Prestamo y la guarda en la base de datos
        prestamo = Prestamo(usuario=user, libro=libro)
        prestamo.save()

        messages.success(request, '¡Préstamo solicitado con éxito!')

    img = "libro.png"
    libros = Libro.objects.all()
    search_term = request.GET.get('search', '')

    if search_term:
        libros = libros.filter(Titulo__icontains=search_term)

    datos = {'libros': libros, 'imagen': img, 'search_term': search_term}
    return render(request, "index.html", datos)

# Este apartado muestra la pagina principal de inicio de sesion, donde si incia con los datos de
# "admin" y la contraseña "libros123" iniciara como admin, y si inicia como un usuario almacenado
# en la base de datos lo mandara al index de usuario.
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'libros123':
            request.session['username'] = 'admin'
            return redirect('index_admin')
        try:
            user = Usuario.objects.get(nombre=username, contraseña=password)
            request.session['username'] = user.nombre
            return redirect('index')
        except Usuario.DoesNotExist:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'iniciar_sesion.html')

# en este apartado el usuario que se registre con los datos correspondientes,
# se almacenara en la base de datos.
def mostrarRegistroUsuario(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        ape_pat = request.POST['apellidoPaterno']
        ape_mat = request.POST['apellidoMaterno']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        correo = request.POST['email']
        nacimiento = request.POST['nacimiento']
        contraseña = request.POST['password']

        #Almacena todos los tados en la variable usuario
        usuario = Usuario(rut=rut, nombre=nombre, ape_pat=ape_pat, ape_mat=ape_mat,
                          direccion=direccion, telefono=telefono, correo=correo,
                          nacimiento=nacimiento, contraseña=contraseña)
        usuario.save()

        messages.success(request, '¡Registro exitoso!')

    return render(request, 'form_registrar.html')

# Muestra el perfil del usuario que inicio sesion, y muestra sus datos de la base de datos.
def MostrarPerfil(request):
    username = request.session.get('username')
    if username:
        try:
            user = Usuario.objects.get(nombre=username)
            usuario_data = {
                'rut': user.rut,
                'nombre': user.nombre,
                'ape_pat': user.ape_pat,
                'ape_mat': user.ape_mat,
                'direccion': user.direccion,
                'telefono': user.telefono,
                'correo': user.correo,
                'nacimiento': user.nacimiento,
            }
            return render(request, 'ver_perfil.html', {'usuario': usuario_data})
        except Usuario.DoesNotExist:
            return render(request, 'error.html', {'mensaje': 'El usuario no existe.'})
    else:
        return redirect('inicio_sesion')

# Muestra el perfil del admin, pero solo muestra su nombre ya que no cuenta con mas datos.
def MostrarPerfilAdmin(request):
    return render(request, 'ver_perfiladmin.html')

# esta funcion sirve para registrar autores en la base de datos.
def mostrarFormRegistroAutor(request):
    if request.method == 'POST':
        nombre_Aut = request.POST['autor']
        autor = Autor(Nombre_Aut=nombre_Aut)
        autor.save()
        messages.success(request, '¡Registro exitoso!')
    return render(request, "form_registrarAutor.html")

# esta funcion sirve para registrar categorias en la base de datos.
def mostrarFormRegistroCategoria(request):
    if request.method == 'POST':
        nombre_Cat = request.POST['categoria']
        categoria = Categoria(Nombre_Cat=nombre_Cat)
        categoria.save()
        messages.success(request, '¡Registro exitoso!')
    return render(request, "form_registrarCategoria.html")

# esta funcion sirve para registrar editoriales en la base de datos.
def mostrarFormRegistroEditorial(request):
    if request.method == 'POST':
        nombre_Edi = request.POST['editorial']
        editorial = Editorial(Nombre_Edi=nombre_Edi)
        editorial.save()
        messages.success(request, '¡Registro exitoso!')
    return render(request, "form_registrarEditorial.html")

# Este apartado es para que el admin pueda registrar a usuarios en la base de datos.
def mostrarRegistroUsuarioAdmin(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        ape_pat = request.POST['apellidoPaterno']
        ape_mat = request.POST['apellidoMaterno']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        correo = request.POST['email']
        nacimiento = request.POST['nacimiento']
        contraseña = request.POST['password']

        #Almacena todos los tados en la variable usuario
        usuario = Usuario(rut=rut, nombre=nombre, ape_pat=ape_pat, ape_mat=ape_mat,
                          direccion=direccion, telefono=telefono, correo=correo,
                          nacimiento=nacimiento, contraseña=contraseña)
        usuario.save()

        messages.success(request, '¡Registro exitoso!')

    return render(request, 'form_registrarUsuarioAdmin.html')

# Muestra los prestamos del usuario que inicio de sesion
def mostrarPrestamos(request):
    username = request.session.get('username')
    if username:
        user = Usuario.objects.get(nombre=username)
        # Filtra los préstamos del usuario actual
        prestamos = Prestamo.objects.filter(usuario=user)
        #libros = Libro.objects.all()
        
        #datos = {'prestamos': prestamos, 'libros': libros}
        datos = {'prestamos': prestamos}
        return render(request, 'prestamos.html', datos)
    else:
        # Manejar el caso cuando no hay un usuario autenticado
        messages.success(request, '¡Usuario no autenticado!')

# Muestra los prestamos de todos los usuarios ademas de mostrar
# los libros actuales en la base de datos
def mostrarPrestamosAdmin(request):
    prestamos = Prestamo.objects.all()
    libros = Libro.objects.all()
    datos = {'prestamos': prestamos, 'libros':libros}
    return render(request, 'prestamosAdmin.html',datos)

# Elimina el prestamo de un usuario de la base de datos.
def eliminarPrestamo(request, id):
    pre = Prestamo.objects.get(id=id)
    pre.delete()
    return redirect('mostrar_prestamosAdmin')

# En este apartado muestra el formulario para registrar libros y almacenarlos en la base de datos.
def mostrarFormRegistrarLibro(request):
    if request.method == 'POST':
        Titulo = request.POST['nlib']
        Num_Ser = request.POST['lser']
        Publicacion = request.POST['lpublicacion']
        autor_id = request.POST['lautor']
        categoria_id = request.POST['lcat']
        editorial_id = request.POST['ledi']
        try:
            autor = Autor.objects.get(id=autor_id)
            categoria = Categoria.objects.get(id=categoria_id)
            editorial = Editorial.objects.get(id=editorial_id)

            #Almacena todos los tados en la variable libro
            libro = Libro(Titulo=Titulo, Num_Ser=Num_Ser, autor=autor, Publicacion=Publicacion, categoria=categoria, editorial=editorial)
            libro.save()
            messages.success(request, '¡Registro exitoso!')
        except Autor.DoesNotExist or categoria.DoesNotExist or editorial.DoesNotExist:
            messages.error(request, 'Error: El autor seleccionado no existe.')

    autores = Autor.objects.all()
    categoria = Categoria.objects.all()
    editorial = Editorial.objects.all()
    
    datos = {'autores': autores, 'categoria': categoria, 'editorial': editorial}

    return render(request, "form_registrarLibro.html", datos)

# Elimina un libro de la base de datos.
def eliminar_libro(request, libro_id):
    libro = Libro.objects.get(pk=libro_id)
    libro.delete()
    messages.error(request, '¡Libro eliminado con exito!')
    return redirect('index_admin')


# Permite modificar los libros de la base de datos para actualizar sus valores
def mostrarFormModificarLibro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)

    if request.method == 'POST':
        libro.Titulo = request.POST['Titulo']
        libro.Num_Ser = request.POST['Num_Ser']
        libro.Publicacion = request.POST['Publicacion']
        libro.autor_id = request.POST['autor']
        libro.categoria_id = request.POST['categoria']
        libro.editorial_id = request.POST['editorial']
        
        libro.save()

        messages.success(request, '¡Modificación exitosa!')

    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    editoriales = Editorial.objects.all()
    datos = {'autores': autores, 'categorias': categorias, 'editoriales': editoriales, 'libro': libro}

    return render(request, "mostrarFormModificarLibro.html", datos)


