from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category (models.Model):
    genre = models.CharField(max_length=150)
    description = RichTextField()
    
    def __str__(self):
        return self.genre


    


class Platform (models.Model):
    wheretosee = models.CharField(max_length=150)
    description = RichTextField()

    def __str__(self):
        return self.wheretosee

    


class Serie (models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()
    year_release = models.DateTimeField()
    to_recommend = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    image = models.ImageField(default='null')
    user = models.ForeignKey(User, editable=False, default=False, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    platform = models.ManyToManyField(Platform)

    def __str__(self):
        return self.title





