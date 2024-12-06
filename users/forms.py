from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'role': 'Rol',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'role': 'Rol',
        }
