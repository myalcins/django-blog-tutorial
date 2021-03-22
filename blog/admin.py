from blog.models import Category, Article, Comment
from django.contrib import admin


admin.site.register(Category)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ('title', 'created_at', 'modified_at')

admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('owner__username', 'article__title')
    list_display = ('article', 'owner', 'created_at')

admin.site.register(Comment, CommentAdmin)