from django.shortcuts import redirect, get_object_or_404
from blog.models import Comment
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse


class CommentDeleteView(DeleteView):
    template_name = 'pages/article-delete.html'
    

    
    def get_object(self):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('id'), owner=self.request.user)
        return comment
    
    def get_success_url(self):
        messages.success(self.request, "Comment succesfully deleted.")
        return reverse('article-detail', kwargs={
            "slug": self.get_object().article.slug,
        })