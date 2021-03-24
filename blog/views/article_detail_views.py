from django.shortcuts import render, get_object_or_404
from blog.models import Article
from blog.forms import CommentForm


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()    
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.owner = request.user
            comment.article = article
            comment.save()
    comment_form = CommentForm()


    return render(request, 'pages/article-detail.html', context={
        "article": article,
        "comments": comments,
        "comment_form": comment_form
    })