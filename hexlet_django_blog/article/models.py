from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=200)  # название статьи
    body = models.TextField()                 # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания
    updated_at = models.DateTimeField(auto_now=True)      # дата последнего изменения
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
