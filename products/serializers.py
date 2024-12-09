from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'active_ingredient', 'presentation', 'category', 'status', 'indications', 'sanitary_registration', 'url', 'image', 'prospect_pdf']
