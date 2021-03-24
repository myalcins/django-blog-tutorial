from django.urls import path
from blog.views import article_detail, homepage, category, user_articles, contact, create_article, edit_article, delete_article

urlpatterns = [
    path('', homepage, name="homepage"),
    path('category/<slug:slug>', category, name="category"),
    path('my/articles', user_articles, name="user-articles"),
    path('article/<slug:slug>', article_detail, name="article-detail"),
    path('contact', contact, name="contact"),
    path('article/create/', create_article, name="create-article"),
    path('article/edit/<slug:slug>', edit_article, name="edit-article"),
    path('article/delete/<slug:slug>', delete_article, name="delete-article")


]
