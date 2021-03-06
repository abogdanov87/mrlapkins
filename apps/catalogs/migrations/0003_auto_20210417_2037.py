# Generated by Django 2.2.6 on 2021-04-17 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0002_auto_20210417_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coatcolor',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coat_color', to='catalogs.Breed', verbose_name='Порода'),
        ),
        migrations.AlterField(
            model_name='eyecolor',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eye_color', to='catalogs.Breed', verbose_name='Порода'),
        ),
    ]
