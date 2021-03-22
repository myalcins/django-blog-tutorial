from blog.models.abstract_date_models import DateAbstractModel
from django.db import models
from django.conf import settings
from blog.models import Article


class Comment(DateAbstractModel):
    content = models.TextField()

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return self.article.title