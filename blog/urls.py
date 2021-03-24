from django.urls import path
from blog.views import article_detail, homepage, category, user_articles, contact, create_article, edit_article, delete_article, delete_comment
from blog.views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('category/<slug:slug>', category, name="category"),
    path('me/articles', user_articles, name="user-articles"),
    path('contact', contact, name="contact"),
    path('article/create/', create_article, name="create-article"),
    path('article/edit/<slug:slug>', edit_article, name="edit-article"),
    path('article/delete/<slug:slug>', delete_article, name="delete-article"),
    path('comment/delete/<int:id>', delete_comment, name="delete-comment"),

    path('', ArticleListView.as_view(), name="homepage"),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name="article-detail")


]
