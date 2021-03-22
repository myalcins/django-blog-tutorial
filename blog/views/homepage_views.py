from django.shortcuts import render
from blog.models import Article 
from django.core.paginator import Paginator


def homepage(request):
    articles = Article.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)


    return render(request, 'pages/homepage.html', context={
        "articles": paginator.get_page(page)
    })