from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('<int:pk>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path('no_permitido/', views.no_permitido, name='no_permitido'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),
]
