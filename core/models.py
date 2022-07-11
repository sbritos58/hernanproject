from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    link = models.URLField()
    slug = models.SlugField()
    media = models.FileField(upload_to="imageArticles/")

    def __str__(self):
        return self.title