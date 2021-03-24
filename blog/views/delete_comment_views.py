from django.shortcuts import redirect, get_object_or_404
from blog.models import Comment
from django.contrib import messages


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id, owner=request.user)
    comment.delete()
    messages.success(request, "Comment succesfully deleted.")
    return redirect('article-detail', slug=comment.article.slug)