from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto
from .forms import ProductoForm

# Create your views here.


def index(request):
    return render(request, 'index.html')  # Asegúrate de que 'index.html' está en la carpeta correcta

# Verifica si el usuario es administrador
#def es_admin(user):
   # return user.is_superuser

# Vista para agregar producto
#@login_required
#@user_passes_test(es_admin)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')  # Redirige a la lista de productos
    else:
        form = ProductoForm()
    return render(request, 'admin/agregar_producto.html', {'form': form})

# Vista para editar producto
#@login_required
#@user_passes_test(es_admin)
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')  # Redirige a la lista de productos
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'admin/editar_producto.html', {'form': form, 'producto': producto})

# Vista para eliminar producto
#@login_required
#@user_passes_test(es_admin)
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')  # Redirige a la lista de productos
    return render(request, 'admin/eliminar_producto.html', {'producto': producto})

# Vista para listar productos
#@login_required
#@user_passes_test(es_admin)
def listar_productos(request):
    return render(request, 'listar_productos.html')
