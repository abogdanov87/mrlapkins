# Generated by Django 2.2.6 on 2021-05-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0009_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='label',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Заголовок'),
        ),
    ]
