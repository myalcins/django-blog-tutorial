from django.db.models import query
from django.urls import base
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
from blog.tasks import scheduled_post
from django.core import serializers
from account.models import User
from django.core.files.storage import FileSystemStorage

class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'pages/article-list.html'
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
    template_name = 'pages/confirm-delete.html'
    success_url = reverse_lazy('user-articles')

    def get_queryset(self):
        article = Article.objects.filter(slug=self.kwargs.get('slug'), owner=self.request.user)
        return article


class ArticleFormView(FormView):
    template_name = "pages/form.html"
    form_class = ArticleForm
    success_url = reverse_lazy('user-articles')

    def form_valid(self, form):
        
        if form.cleaned_data.get('schedule_time'):
            
            image = form.cleaned_data.get('image')
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category = serializers.serialize('json', form.cleaned_data.get('category'), fields=('id',))
            owner = serializers.serialize('json', User.objects.filter(id=self.request.user.id), fields=('id',))
            
            fs = FileSystemStorage(location='media/article_images', base_url='article_images')
            image = fs.save(str(image), image)
            image_url = fs.url(image)

            scheduled_post.apply_async(kwargs={"title": title, 
                                        "content": content,
                                        "category": category,
                                        "owner": owner,
                                        "image": image_url}, eta=form.cleaned_data.get('schedule_time'))
            return redirect(self.success_url)

        else:
            article = form.save(commit=False) 
            article.owner = self.request.user
            article.save()
            form.save_m2m()
            return redirect(self.success_url)


class ArticleUptadeView(UpdateView):
    template_name = 'pages/form.html'
    fields = ('title', 'content', 'image', 'category')

    def get_object(self):
        return get_object_or_404(Article, slug=self.kwargs.get('slug'), owner=self.request.user)

    def get_success_url(self) -> str:
        return reverse('article-detail', kwargs={
            "slug": self.get_object().slug
        })