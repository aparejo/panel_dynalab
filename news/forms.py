from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'tags', 'scheduled_date', 'image_url']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'category': 'Categoría',
            'tags': 'Etiquetas',
            'scheduled_date': 'Fecha Programada',
            'image_url': 'URL de la Imagen',
        }
