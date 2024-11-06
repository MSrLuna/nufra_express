# forms.py
from django import forms
from .models import Producto, Usuario
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'email', 'telefono', 'direccion', 'password', 'rol']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'precio_unitario', 'disponible']
