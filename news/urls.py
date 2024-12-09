from django.urls import path
from . import views
from .views import NewsListAPIView

app_name = 'news'

urlpatterns = [
    path('', views.lista_noticias, name='lista_noticias'),
    path('crear/', views.crear_noticia, name='crear_noticia'),
    path('<int:pk>/editar/', views.editar_noticia, name='editar_noticia'),
    path('<int:pk>/eliminar/', views.eliminar_noticia, name='eliminar_noticia'),
    
    path('api/', NewsListAPIView.as_view(), name='news_list_api'),
    
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
    path('crear/', views.crear_noticia, name='crear_noticia'),
    
]
