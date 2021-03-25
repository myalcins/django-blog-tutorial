from django.urls import path
from blog.views import (ArticleListView, 
                    ArticleDetailView, 
                    ArticleDeleteView, 
                    ArticleFormView, 
                    ContactFormView, 
                    CategoriesArticleListView, 
                    ArticleUptadeView, 
                    CommentDeleteView)
                    

urlpatterns = [
    
    path('', ArticleListView.as_view(), name="homepage"),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name="article-detail"),
    path('article/delete/<slug:slug>', ArticleDeleteView.as_view(), name="article-delete"),
    path('article/create/', ArticleFormView.as_view(), name="article-create"),
    path('article/edit/<slug:slug>', ArticleUptadeView.as_view(), name="article-edit"),

    path('comment/delete/<int:id>', CommentDeleteView.as_view(), name="comment-delete"),


    path('contact/', ContactFormView.as_view(), name="contact"),
    path('category/<slug:slug>', CategoriesArticleListView.as_view(), name="category"),
]
