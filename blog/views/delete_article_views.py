from django.contrib.auth.decorators import login_required
from blog.models import Article
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def delete_article(request, slug):
    get_object_or_404(Article, slug=slug, owner=request.user).delete()
    return redirect('user-articles')
