from django.shortcuts import redirect, get_object_or_404
from blog.models import Comment



def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id, owner=request.user)
    comment.delete()
    return redirect('article-detail', slug=comment.article.slug)