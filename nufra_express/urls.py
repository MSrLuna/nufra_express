from django.contrib import admin
from django.urls import path
from app.views import home_view, register_view, login_view, categoria_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('categoria/<slug:categoria>/', categoria_view, name='categoria'),  # Modifica la URL para aceptar un argumento
]
