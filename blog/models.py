from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField(max_length=255)
    auteur = models.CharField( max_length=50)

    class Meta:
        verbose_name = "Article"
    def __str__(self):
        return self.title
    