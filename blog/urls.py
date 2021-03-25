from django.urls import path
from blog.views import delete_comment
from blog.views import ArticleListView, ArticleDetailView, ArticleDeleteView, ArticleFormView, ContactFormView, CategoriesArticleListView, ArticleUptadeView


urlpatterns = [
    path('comment/delete/<int:id>', delete_comment, name="delete-comment"),
    path('', ArticleListView.as_view(), name="homepage"),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name="article-detail"),
    path('article/delete/<slug:slug>', ArticleDeleteView.as_view(), name="article-delete"),
    path('article/create/', ArticleFormView.as_view(), name="article-create"),
    path('article/edit/<slug:slug>', ArticleUptadeView.as_view(), name="article-edit"),


    path('contact/', ContactFormView.as_view(), name="contact"),
    path('category/<slug:slug>', CategoriesArticleListView.as_view(), name="category"),


]
