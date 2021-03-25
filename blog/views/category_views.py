from django.shortcuts import get_object_or_404
from blog.models import Category 
from django.views.generic import ListView
from django.db.models import Q



class CategoriesArticleListView(ListView):
    template_name = 'pages/article-list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        category =  Category.objects.prefetch_related('articles').get(slug=self.kwargs.get('slug'))
        articles = category.articles.all()
        return articles