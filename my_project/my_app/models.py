from django.db import models

# Create your models here.

class NewsFilms(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    images = models.ImageField(blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)
    img_url = models.CharField(max_length=1000)


class Person(models.Model):
    pass
