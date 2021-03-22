from blog.models import Category, Article
from django.contrib import admin


admin.site.register(Category)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ('title', 'created_at', 'modified_at')

admin.site.register(Article, ArticleAdmin)