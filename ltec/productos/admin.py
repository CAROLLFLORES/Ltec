
from django.contrib import admin
from .models import Categoria, Producto  # Importa los modelos de la aplicación actual

# Inline para gestionar productos en la página de categorías
class ProductoInline(admin.TabularInline):
    model = Producto
    fields = ('nombre', 'precio', 'stock', 'activo', 'imagen')
    extra = 1  # Número de filas vacías para agregar nuevos productos
    min_num = 1  # Mínimo de productos por categoría
    max_num = 10  # Máximo de productos por categoría
    show_change_link = True  # Permite editar productos desde aquí
    classes = ('collapse',)  # Opcional: permite colapsar la tabla

# Administración de categorías
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    inlines = [ProductoInline]

# Administración de productos
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'activo')
    list_editable = ('precio', 'stock', 'activo')
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'descripcion')
