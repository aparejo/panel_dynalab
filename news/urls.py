from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.lista_noticias, name='lista_noticias'),
    path('crear/', views.crear_noticia, name='crear_noticia'),
    path('<int:pk>/editar/', views.editar_noticia, name='editar_noticia'),
    path('<int:pk>/eliminar/', views.eliminar_noticia, name='eliminar_noticia'),
]
