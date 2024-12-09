from django import forms
from .models import News, NewsCategory

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'tags', 'scheduled_date', 'image']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'category': 'Categoría',
            'tags': 'Etiquetas',
            'scheduled_date': 'Fecha Programada',
            'image': 'Imagen',
        }
        widgets = {
            'scheduled_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: noticia, evento, destacada'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
        
class NewsCategoryForm(forms.ModelForm):
    class Meta:
        model = NewsCategory
        fields = ['name', 'description']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
