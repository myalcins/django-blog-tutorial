from django.shortcuts import render, get_object_or_404
from blog.models import Category 
from django.core.paginator import Paginator


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)


    return render(request, 'pages/category.html', context={
        "articles": paginator.get_page(page),
        "title": category.title 
    })