from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'active_ingredient', 'presentation', 'category', 'status', 'indications', 'sanitary_registration', 'url', 'image', 'prospect_pdf']

class CategorySerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'description']  # Incluye el ícono
        
    def get_icon(self, obj):
        if obj.icon:
            request = self.context.get('request')  # Para obtener la URL completa
            return request.build_absolute_uri(obj.icon.url)
        return None