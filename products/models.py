from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    active_ingredient = models.CharField(max_length=255)
    presentation = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    status = models.BooleanField(default=True)
    indications = models.TextField()
    sanitary_registration = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)  # Campo para imágenes
    prospect_pdf = models.FileField(upload_to='products/prospectus/', blank=True, null=True)  # Campo para PDFs

    def __str__(self):
        return self.name
