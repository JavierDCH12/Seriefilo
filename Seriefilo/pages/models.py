from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Page (models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    slug = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

