from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from app.views import home_view, register_view, login_view, categoria_view, agregar_producto, agregar_a_carrito, ver_carrito, eliminar_del_carrito
from nufra_express import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='Login'),
    path('register/', register_view, name='register'),
    path('categoria/<slug:categoria>/', categoria_view, name='categoria'),  # Modifica la URL para aceptar un argumento
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('agregar_a_carrito/<int:producto_id>/', agregar_a_carrito, name='agregar_a_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:carrito_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
]

# Agregar configuración para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)