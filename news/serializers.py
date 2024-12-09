from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')  # Para incluir el nombre de la categoría

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'category', 'category_name', 'tags', 'scheduled_date', 'image']
