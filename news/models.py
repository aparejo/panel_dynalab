from django.db import models
class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name="news")
    tags = models.CharField(max_length=255, blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
