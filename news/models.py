from django.db import models
from products.models import Category  # Ajusta según la ubicación de Category

class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('NewsCategory', on_delete=models.CASCADE, related_name='news')  # Relación con NewsCategory
    tags = models.CharField(max_length=255, blank=True, null=True)
    scheduled_date = models.DateField()
    image = models.ImageField(upload_to='news/images/', blank=True, null=True)  # Campo para subir imagenes

    def __str__(self):
        return self.title
