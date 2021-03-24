from django.shortcuts import render, redirect
from blog.forms import ArticleForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def create_article(request):
    form = ArticleForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.owner = request.user
        article.save()
        form.save_m2m()
        return redirect('article-detail', slug=article.slug)
    return render(request, 'pages/create-article.html', context={
        "form": form
    })