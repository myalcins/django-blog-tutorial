from django.db.models import query
from django.views.generic import ListView, CreateView, DeleteView, FormView
from blog.models import Article, Comment
from blog.forms import ArticleForm, CommentForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages 


class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'pages/homepage.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('query'):
            query = self.request.GET.get("query")
            queryset = self.queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
            return queryset
        else:
            return self.queryset


class ArticleDetailView(View):
    http_method_names = ['get', 'post']
    comment_form = CommentForm

    def get(self, request, slug):
        article = Article.objects.prefetch_related('comments').get(slug=slug)
        comments = article.comments.all()
        return render(request, 'pages/article-detail.html', context={
            "article": article,
            "comments": comments,
            "comment_form": self.comment_form,
        })

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        comment_form = self.comment_form(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.owner = request.user
            comment.article = article
            comment.save()
            messages.success(request, "Comment successfully created.")
        return redirect('article-detail', slug)