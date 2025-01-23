from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto
from .forms import ProductoForm

# Create your views here.
from .models import Categoria

@login_required
def panel_admin(request):
    return render(request, 'productos/admin_panel.html')



def index(request):
    categorias = Categoria.objects.prefetch_related('productos').all()
    context = {
        'cuerdas': Producto.objects.filter(categoria__nombre="Cuerdas"),
        'cuerdas_perfiladas': Producto.objects.filter(categoria__nombre="cuerdas perfiladas"),
        'hibrido': Producto.objects.filter(categoria__nombre__iexact="Híbrido"),
        'accesorios': Producto.objects.filter(categoria__nombre="Accesorios"),
        'promociones': Producto.objects.filter(categoria__nombre="Promociones"),
    }
    return render(request, 'index.html', context)

#@login_required
#def listar_productos(request):
    #productos = Producto.objects.all()  # Asegúrate de que haya productos en la base de datos
   # return render(request, 'listar_productos.html', {'productos': productos})

@login_required
def listar_productos(request):
    productos = Producto.objects.all()  # Asegúrate de que estás obteniendo todos los productos
    return render(request, 'listar_productos.html', {'productos': productos})


@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})


@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})