from blog.models.abstract_date_models import DateAbstractModel
from django.db import models
from autoslug import AutoSlugField
from blog.models import Category
from django.conf import settings
from ckeditor.fields import RichTextField


class Article(DateAbstractModel):
    title = models.CharField(max_length=50)
    content = RichTextField()
    slug = AutoSlugField(populate_from="title", unique=True)
    image = models.ImageField(upload_to="article_images")

    categories = models.ManyToManyField(Category, related_name="articles")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="articles",
                            on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "article"
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title