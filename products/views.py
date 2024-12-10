from django.shortcuts import render, redirect, get_object_or_404
from users.middleware import role_required
from django.http import HttpResponse
from .models import Product, Category
from django.db.models import Q
from .forms import ProductForm, CategoryForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer

# Listar productos
@role_required(allowed_roles=['admin', 'editor'])
def lista_productos(request):
    productos = Product.objects.all()
    return render(request, 'products/lista_productos.html', {'productos': productos})

@role_required(allowed_roles=['admin', 'editor'])
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

@role_required(allowed_roles=['admin', 'editor'])
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

@role_required(allowed_roles=['admin', 'editor'])
# Eliminar producto
def eliminar_producto(request, pk):
    producto = Product.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('products:lista_productos')
    return render(request, 'products/confirmar_eliminar_producto.html', {'producto': producto})


@role_required(allowed_roles=['admin', 'editor'])
# Listar Categorías
def lista_categorias(request):
    categorias = Category.objects.all()
    return render(request, 'products/lista_categorias.html', {'categorias': categorias})

@role_required(allowed_roles=['admin', 'editor'])
# Crear Categoría
def crear_categoria(request):
    if request.method == 'POST':
        formulario = CategoryForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('products:lista_categorias')
    else:
        formulario = CategoryForm()
    return render(request, 'products/formulario_categoria.html', {'formulario': formulario})

@role_required(allowed_roles=['admin', 'editor'])
# Editar Categoría
def editar_categoria(request, pk):
    categoria = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        formulario = CategoryForm(request.POST, request.FILES, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('products:lista_categorias')
    else:
        formulario = CategoryForm(instance=categoria)
    return render(request, 'products/formulario_categoria.html', {'formulario': formulario, 'categoria': categoria})

@role_required(allowed_roles=['admin', 'editor'])
# Eliminar Categoría
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('products:lista_categorias')
    return render(request, 'products/confirmar_eliminar_categoria.html', {'categoria': categoria})

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    
class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)

def buscar_productos(request):
    query = request.GET.get('q', '')  # Obtén el término de búsqueda del campo "q"
    resultados = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    ) if query else Product.objects.all()

    context = {
        'resultados': resultados,
        'query': query,
    }
    return render(request, 'products/buscar.html', context)