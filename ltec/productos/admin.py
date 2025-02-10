
from django.contrib import admin
from .models import Categoria, Producto  # Importa los modelos de la aplicación actual

class ProductoInline(admin.TabularInline):
    model = Producto
    fields = ('nombre', 'precio', 'activo', 'imagen')
    extra = 1  # Permite agregar productos en línea

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    inlines = [ProductoInline]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'activo')
    list_editable = ('precio', 'activo')
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'descripcion')
