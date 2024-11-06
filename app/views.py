from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProductoForm
from .models import CarroCompra, Producto, CategoriaProducto
from django.utils import timezone

def home_view(request):
    categorias = CategoriaProducto.objects.all()  # Obtener todas las categorías
    productos = Producto.objects.filter(disponible=True)  # Obtener productos disponibles
    context = {
        'categorias': categorias,
        'productos': productos,
    }
    return render(request, 'home.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def categoria_view(request, categoria):
    # Aquí puedes obtener y pasar los productos de la categoría a la plantilla
    return render(request, 'categoria.html', {'categoria': categoria})  # Pasa la categoría a la plantilla

def agregar_producto(request):
    # Si es una solicitud GET, mostramos el formulario vacío
    if request.method == 'GET':
        # Obtener todas las categorías disponibles para mostrarlas en el formulario
        categorias = CategoriaProducto.objects.filter(disponible=True)
        return render(request, 'agregar_producto.html', {'categorias': categorias})

    # Si es una solicitud POST, procesamos el formulario
    elif request.method == 'POST':
        nombre = request.POST['nombre']
        categoria_id = request.POST['categoria']
        descripcion = request.POST['descripcion']
        precio_unitario = request.POST['precio_unitario']
        imagen = request.FILES.get('imagen', None)
        fecha_ingreso = timezone.now().date()  # Fecha actual

        # Crear el producto
        producto = Producto(
            nombre=nombre,
            categoria_id=categoria_id,
            descripcion=descripcion,
            precio_unitario=precio_unitario,
            imagen=imagen,
            fecha_ingreso=fecha_ingreso
        )
        producto.save()

        # Redirigir a la página de productos (o cualquier otra página que desees)
        return redirect('home')  # Asegúrate de tener una vista de lista de productos

    # Si no es GET ni POST, también puede devolver una respuesta adecuada (aunque no debería ocurrir)
    return redirect('home')  # O la URL que desees como predeterminada

def agregar_a_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        total = producto.precio_unitario * cantidad

        if CarroCompra.objects.filter(usuario_id=request.user, producto=producto).exists():
            carrito = CarroCompra.objects.get(usuario_id=request.user, producto=producto)
            carrito.cantidad += cantidad
            carrito.total = carrito.cantidad * producto.precio_unitario
            carrito.save()
        else:
            CarroCompra.objects.create(
                usuario_id=request.user,
                producto=producto,
                cantidad=cantidad,
                total=total
            )

        return redirect('ver_carrito')

def ver_carrito(request):
    carrito_items = CarroCompra.objects.filter(usuario_id=request.user)
    total_carrito = sum(item.total for item in carrito_items)
    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total_carrito': total_carrito})

def eliminar_del_carrito(request, carrito_id):
    carrito_item = get_object_or_404(CarroCompra, id=carrito_id, usuario_id=request.user)
    carrito_item.delete()
    return redirect('ver_carrito')