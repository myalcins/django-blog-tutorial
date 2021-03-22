from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):

    title = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='title', unique=True)

    class Meta:
        db_table = "category"
        verbose_name_plural = "Categorys"
        verbose_name = "Category"

    def __str__(self) -> str:
        return self.title