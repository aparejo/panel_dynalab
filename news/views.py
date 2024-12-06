from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from users.middleware import role_required

@role_required(allowed_roles=['admin', 'editor'])
def lista_noticias(request):
    noticias = News.objects.all()
    return render(request, 'news/lista_noticias.html', {'noticias': noticias})

# Listar noticias
def lista_noticias(request):
    noticias = News.objects.all()
    return render(request, 'news/lista_noticias.html', {'noticias': noticias})

# Crear noticia
def crear_noticia(request):
    if request.method == 'POST':
        formulario = NewsForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('news:lista_noticias')
    else:
        formulario = NewsForm()
    return render(request, 'news/formulario_noticia.html', {'formulario': formulario})

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

# Eliminar noticia
def eliminar_noticia(request, pk):
    noticia = News.objects.get(pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('news:lista_noticias')
    return render(request, 'news/confirmar_eliminar_noticia.html', {'noticia': noticia})
