from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True, verbose_name="Image URL")  # <-- INI YANG BENAR
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['-created_at']