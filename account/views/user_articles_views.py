from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def user_articles(request):
    articles = request.user.articles.all()
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)


    return render(request, 'pages/user-articles.html', context={
        "articles": paginator.get_page(page),
        "title": request.user.username
    })