from django.db.models import query
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, FormView
from django.views.generic.edit import UpdateView
from blog.models import Article, Comment
from blog.forms import ArticleForm, CommentForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages 
from django.urls import reverse


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


class ArticleDeleteView(DeleteView):
    template_name = 'pages/article-delete.html'
    success_url = reverse_lazy('user-articles')

    def get_queryset(self):
        article = Article.objects.filter(slug=self.kwargs.get('slug'), owner=self.request.user)
        return article


class ArticleFormView(FormView):
    template_name = "pages/article-create.html"
    form_class = ArticleForm
    success_url = reverse_lazy('user-articles')

    def form_valid(self, form):
        article = form.save(commit=False) 
        article.owner = self.request.user
        article.save()
        form.save_m2m()
        return redirect(self.success_url)


class ArticleUptadeView(UpdateView):
    template_name = 'pages/article-edit.html'
    fields = ('title', 'content', 'image', 'category')

    def get_object(self):
        return get_object_or_404(Article, slug=self.kwargs.get('slug'), owner=self.request.user)

    def get_success_url(self) -> str:
        return reverse('article-detail', kwargs={
            "slug": self.get_object().slug
        })