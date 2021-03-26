from celery import shared_task
from blog.models import Article, Category
from django.db.models.fields.files import ImageFieldFile
from account.models import User
from django.core import serializers



@shared_task
def scheduled_post(**kwargs):
    
    for user in serializers.deserialize('json', kwargs['owner']):
        user = User.objects.get(pk=user.object.pk)
        
    article = Article(title=kwargs['title'],
                    owner=user,
                    content=kwargs['content'],
                    image=kwargs['image'])
    article.save()

    for category in serializers.deserialize('json', kwargs['category']):
        category = Category.objects.get(pk=category.object.pk)
        article.category.add(category)

    return None