from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category
from .forms import ProductForm

# Listar productos
def lista_productos(request):
    productos = Product.objects.all()
    return render(request, 'products/lista_productos.html', {'productos': productos})

# Crear producto
def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductForm(request.POST, request.FILES)  # Agregar request.FILES para manejar archivos
        if formulario.is_valid():
            formulario.save()
            return redirect('products:lista_productos')
    else:
        formulario = ProductForm()
    return render(request, 'products/formulario_producto.html', {'formulario': formulario})

# Editar producto
def editar_producto(request, pk):
    producto = Product.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = ProductForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('products:lista_productos')
    else:
        formulario = ProductForm(instance=producto)
    return render(request, 'products/formulario_producto.html', {'formulario': formulario})

# Eliminar producto
def eliminar_producto(request, pk):
    producto = Product.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('products:lista_productos')
    return render(request, 'products/confirmar_eliminar_producto.html', {'producto': producto})
