from django import forms
from blog.models import Article


class ArticleForm(forms.ModelForm):
    schedule_time = forms.DateTimeField(required=False ,input_formats=['%Y/%m/%d %H:%M'])

    class Meta:
        model = Article
        fields = (
                'image',
                'title',
                'content',
                'category',
                'schedule_time'
                )
