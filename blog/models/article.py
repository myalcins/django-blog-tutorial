from enum import unique
from django.db import models
from autoslug import AutoSlugField
from blog.models import Category
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    image = models.ImageField(upload_to="article_images")

    categorys = models.ManyToManyField(Category, related_name="articles")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="articles",
                            on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "article"