# productos/urls.py
from django.urls import path
from .views import listar_productos  # Cambié la importación a un formato correcto
from . import views
from .views import panel_admin  # La vista del panel de administración
from .views_auth import login_view, logout_view
from productos import views  # Importa tus vistas
from django.conf.urls.static import static
from django.conf import settings
from . import views  # Importa las vistas de tu aplicación



urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', listar_productos, name='listar_productos'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin-panel/', panel_admin, name='panel_admin'),  # Ruta protegida
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
    
    
 #Agregar solo en modo desarrollo para servir archivos estáticos y multimedia

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

