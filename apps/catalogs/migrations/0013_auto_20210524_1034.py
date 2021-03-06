# Generated by Django 2.2.6 on 2021-05-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0012_auto_20210516_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coatcolor',
            name='base_color',
            field=models.CharField(choices=[('n', 'Чёрный'), ('n.1', 'Сил'), ('n.2', 'Коричневый'), ('n.3', 'Дикий'), ('n.4', 'Рыжевато-коричневый'), ('a', 'Голубой'), ('b', 'Шоколадный'), ('c', 'Лиловый'), ('d', 'Красный'), ('e', 'Кремовый'), ('f', 'Черный черепаховый'), ('g', 'Голубой черепаховый'), ('h', 'Шоколадный черепаховый'), ('j', 'Лиловый черепаховый'), ('o', 'Циннамон, соррель'), ('p', 'Фавн'), ('q', 'Циннамон черепаховый'), ('r', 'Фавн черепаховый'), ('w', 'Белый'), ('nt', 'Янтарный'), ('at', 'Светло-янтарный'), ('dt', 'Красный-янтарный'), ('et', 'Кремовый-янтарный'), ('ft', 'Янтарный черепаховый'), ('gt', 'Светло-янтарный черепаховый')], default='n', max_length=30, verbose_name='Основной цвет'),
        ),
    ]
