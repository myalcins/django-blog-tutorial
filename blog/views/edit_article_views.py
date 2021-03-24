from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from blog.models import Article


@login_required(login_url='/')
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug, owner=request.user)
    form = ArticleForm(request.POST or None, files=request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article-detail', slug=article.slug)
    return render(request, 'pages/edit-article.html', context={
        "form": form
    })  