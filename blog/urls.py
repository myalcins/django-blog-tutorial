from django.urls import path
from blog.views.homepage_views import homepage 
from blog.views.category_views import category
from blog.views.user_articles_views import user_articles


urlpatterns = [
    path('', homepage, name="homepage"),
    path('category/<slug:slug>', category, name="category"),
    path('my/articles', user_articles, name="user_articles")
]
