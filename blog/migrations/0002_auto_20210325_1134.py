# Generated by Django 3.1.7 on 2021-03-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='article_list', to='blog.Category'),
        ),
    ]
