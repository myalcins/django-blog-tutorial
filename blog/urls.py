from django.urls import path
from blog.views import article_detail, homepage, category, user_articles, contact

urlpatterns = [
    path('', homepage, name="homepage"),
    path('category/<slug:slug>', category, name="category"),
    path('my/articles', user_articles, name="user_articles"),
    path('article/<slug:slug>', article_detail, name="article_detail"),
    path('contact', contact, name="contact"),
]
