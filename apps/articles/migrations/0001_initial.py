# Generated by Django 2.2.6 on 2021-06-09 19:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogs', '0013_auto_20210524_1034'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('alias', models.CharField(max_length=500, verbose_name='Псевдоним')),
                ('body', djrichtextfield.models.RichTextField(default='', verbose_name='Текст')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Создана')),
                ('source', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Источник')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликована')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='ArticleBreed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(db_column='article_id', on_delete=django.db.models.deletion.PROTECT, to='articles.Article', verbose_name='Статья')),
                ('breed', models.ForeignKey(db_column='breed_id', on_delete=django.db.models.deletion.PROTECT, to='catalogs.Breed', verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Статья - Порода',
                'verbose_name_plural': 'Статьи - Породы',
                'db_table': 'article_breed',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='breed',
            field=models.ManyToManyField(related_name='article_breed', through='articles.ArticleBreed', to='catalogs.Breed', verbose_name='Порода'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='article', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
