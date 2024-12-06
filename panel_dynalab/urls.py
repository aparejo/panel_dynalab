from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('news/', include('news.urls')),  # Incluye las URLs de noticias
    path('users/', include('users.urls')),
    path('', lambda request: redirect('users:dashboard')),  # Redirigir al Dashboard
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)