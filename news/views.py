from django.shortcuts import render, redirect, get_object_or_404
from .models import News, NewsCategory
from .forms import NewsForm, NewsCategoryForm
from users.middleware import role_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NewsSerializer

@role_required(allowed_roles=['admin', 'editor'])
def lista_noticias(request):
    noticias = News.objects.all()
    return render(request, 'news/lista_noticias.html', {'noticias': noticias})

@role_required(allowed_roles=['admin', 'editor'])
# Listar noticias
def lista_noticias(request):
    noticias = News.objects.all()
    return render(request, 'news/lista_noticias.html', {'noticias': noticias})

@role_required(allowed_roles=['admin', 'editor'])
# Crear noticia
def crear_noticia(request):
    if request.method == 'POST':
        formulario = NewsForm(request.POST, request.FILES)  # Incluye request.FILES para manejar archivos
        if formulario.is_valid():
            formulario.save()
            return redirect('news:lista_noticias')
    else:
        formulario = NewsForm()
    return render(request, 'news/formulario_noticia.html', {'formulario': formulario})

@role_required(allowed_roles=['admin', 'editor'])
# Editar noticia
def editar_noticia(request, pk):
    noticia = News.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = NewsForm(request.POST, instance=noticia)
        if formulario.is_valid():
            formulario.save()
            return redirect('news:lista_noticias')
    else:
        formulario = NewsForm(instance=noticia)
    return render(request, 'news/formulario_noticia.html', {'formulario': formulario})

@role_required(allowed_roles=['admin', 'editor'])
# Eliminar noticia
def eliminar_noticia(request, pk):
    noticia = News.objects.get(pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('news:lista_noticias')
    return render(request, 'news/confirmar_eliminar_noticia.html', {'noticia': noticia})

@role_required(allowed_roles=['admin', 'editor'])
# Lista de categorías
def lista_categorias(request):
    categorias = NewsCategory.objects.all()
    return render(request, 'news/lista_categorias.html', {'categorias': categorias})

@role_required(allowed_roles=['admin', 'editor'])
# Crear categoría
def crear_categoria(request):
    if request.method == 'POST':
        formulario = NewsCategoryForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('news:lista_categorias')
    else:
        formulario = NewsCategoryForm()
    return render(request, 'news/formulario_categoria.html', {'formulario': formulario})

@role_required(allowed_roles=['admin', 'editor'])
# Editar categoría
def editar_categoria(request, pk):
    categoria = get_object_or_404(NewsCategory, pk=pk)
    if request.method == 'POST':
        formulario = NewsCategoryForm(request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('news:lista_categorias')
    else:
        formulario = NewsCategoryForm(instance=categoria)
    return render(request, 'news/formulario_categoria.html', {'formulario': formulario})

@role_required(allowed_roles=['admin', 'editor'])
# Eliminar categoría
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(NewsCategory, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('news:lista_categorias')
    return render(request, 'news/confirmar_eliminar_categoria.html', {'categoria': categoria})

class NewsListAPIView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True, context={'request': request})
        return Response(serializer.data)