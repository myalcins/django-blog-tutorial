from blog.models import Category, Article, Comment, Contact
from django.contrib import admin


admin.site.register(Category)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ('title', 'created_at', 'modified_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('owner__username', 'article__title')
    list_display = ('article', 'owner', 'created_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('email', 'title', 'name')
    list_display = ('email', 'name', 'title', 'created_at')
