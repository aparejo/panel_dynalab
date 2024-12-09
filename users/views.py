from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import UserForm, UserEditForm
from products.models import Product
from news.models import News
from users.models import User
from django.contrib import messages

# Listar usuarios

@role_required(allowed_roles=['admin'])
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'users/lista_usuarios.html', {'usuarios': usuarios})

@role_required(allowed_roles=['admin'])
# Crear usuario
def crear_usuario(request):
    if request.method == 'POST':
        formulario = UserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('users:lista_usuarios')
    else:
        formulario = UserForm()
    return render(request, 'users/formulario_usuario.html', {'formulario': formulario})

# Editar usuario
@role_required(allowed_roles=['admin'])
def editar_usuario(request, pk):
    usuario = User.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('users:lista_usuarios')
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'users/formulario_usuario.html', {'formulario': formulario})

@role_required(allowed_roles=['admin'])
# Eliminar usuario
def eliminar_usuario(request, pk):
    usuario = User.objects.get(pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('users:lista_usuarios')
    return render(request, 'users/confirmar_eliminar_usuario.html', {'usuario': usuario})

def no_permitido(request):
    return render(request, 'users/no_permitido.html')

@role_required(allowed_roles=['admin'])
def dashboard(request):
    productos_totales = Product.objects.count()
    noticias_totales = News.objects.count()
    usuarios_totales = User.objects.count()
    return render(request, 'users/dashboard.html', {
        'productos_totales': productos_totales,
        'noticias_totales': noticias_totales,
        'usuarios_totales': usuarios_totales,
    })
    

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:dashboard')  # Redirigir al dashboard
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'users/login.html')  # Usar la nueva plantilla

def cerrar_sesion(request):
    logout(request)
    return redirect('users:login')  # Redirigir al login después de cerrar sesión

def editar_perfil(request):
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('users:editar_perfil')
    else:
        formulario = UserEditForm(instance=request.user)
    return render(request, 'users/editar_perfil.html', {'formulario': formulario})