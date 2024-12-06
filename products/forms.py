from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'active_ingredient', 'presentation', 'category', 'status',
            'indications', 'sanitary_registration', 'url', 'image', 'prospect_pdf'
        ]
        labels = {
            'name': 'Nombre',
            'active_ingredient': 'Principio Activo',
            'presentation': 'Presentación',
            'category': 'Categoría',
            'status': 'Estado',
            'indications': 'Indicaciones',
            'sanitary_registration': 'Registro Sanitario',
            'url': 'URL del Producto',
            'image': 'Imagen del Producto',
            'prospect_pdf': 'Prospecto PDF',
        }
        widgets = {
            'status': forms.Select(choices=[(True, 'Active'), (False, 'Inactive')]),
        }
