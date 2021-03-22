from django.shortcuts import render
from blog.models import Article 
from django.core.paginator import Paginator
from django.db.models import Q


def homepage(request):
    query = request.GET.get("query")
    articles = Article.objects.all()

    if query:
        articles = articles.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()

    page = request.GET.get('page')
    paginator = Paginator(articles, 10)


    return render(request, 'pages/homepage.html', context={
        "articles": paginator.get_page(page)
    })