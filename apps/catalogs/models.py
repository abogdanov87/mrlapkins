import os
from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField
from django.apps import apps
from common.models import Entity, PeriodHistoricalModel
from simple_history.models import HistoricalRecords

from django.utils.translation import gettext_lazy as _


PET_TYPES = (
    ('cat', 'Кошка'),
    ('dog', 'Собака'),
)

RANKS_V1 = (
    (1, 'Очень низкая',),
    (2, 'Низкая',),
    (3, 'Средняя',),
    (4, 'Высокая',),
    (5, 'Очень высокая',),
)

RANKS_V2 = (
    (1, 'Очень низкий',),
    (2, 'Низкий',),
    (3, 'Средний',),
    (4, 'Высокий',),
    (5, 'Очень высокий',),
)

RANKS_V3 = (
    (1, 'Очень плохое'),
    (2, 'Плохое'),
    (3, 'Среднее'),
    (4, 'Хорошее'),
    (5, 'Очень хорошее'),
)

RANKS_V4 = (
    (1, 'Очень низкое',),
    (2, 'Низкое',),
    (3, 'Среднее',),
    (4, 'Высокое',),
    (5, 'Очень высокое',),
)


class Breed(models.Model):
    """
        Порода 
    """
    pet_type = models.CharField(
        _('Вид питомца'),
        max_length=30,
        choices=PET_TYPES,
        blank=False, null=False,
        default='cat'
    )
    alias = models.CharField(
        _('Псевдоним (транслит)'),
        max_length=255,
        blank=False, null=False,
        default='alias',
    )
    title = models.CharField(
        _('Название породы'),
        max_length=255,
        blank=False, null=False,
        default='',
    )
    short_description = models.TextField(
        _('Краткое описание'),
        max_length=256,
        blank=False, null=False,
        default='',
    )
    full_description = models.TextField(
        _('Полное описание'),
        max_length=2000,
        blank=False, null=False,
        default='',
    )
    origin = models.TextField(
        _('Происхождение'),
        max_length=2000,
        blank=False, null=False,
        default='',
    )
    character = models.TextField(
        _('Характер и повадки'),
        max_length=2000,
        blank=False, null=False,
        default='',
    )
    image = ThumbnailerImageField(
        _('Изображение'),
        upload_to ='badges/',
        blank=True, null=True,
        resize_source=dict(size=(320, 320), sharpen=True),
    )
    allergenicity = models.PositiveIntegerField(
        _('Аллергенность'),
        choices=RANKS_V1,
        blank=False, null=False,
        default=3
    )
    molt = models.PositiveIntegerField(
        _('Линька'),
        choices=RANKS_V1,
        blank=False, null=False,
        default=3
    )
    intelligence = models.PositiveIntegerField(
        _('Интеллект'),
        choices=RANKS_V2,
        blank=False, null=False,
        default=3
    )
    sociability = models.PositiveIntegerField(
        _('Общительность'),
        choices=RANKS_V1,
        blank=False, null=False,
        default=3
    )
    need_for_care = models.PositiveIntegerField(
        _('Потребность в уходе'),
        choices=RANKS_V1,
        blank=False, null=False,
        default=3
    )
    activity = models.PositiveIntegerField(
        _('Активность'),
        choices=RANKS_V1,
        blank=False, null=False,
        default=3
    )
    friendliness = models.PositiveIntegerField(
        _('Дружелюбие'),
        choices=RANKS_V4,
        blank=False, null=False,
        default=3
    )
    health = models.PositiveIntegerField(
        _('Здоровье'),
        choices=RANKS_V3,
        blank=False, null=False,
        default=3
    )
    active = models.BooleanField(
        _('Статус активности'),
        blank=False, null=False,
        default=True,
    )
    history = HistoricalRecords()

    class Meta:
        db_table = 'breed'
        verbose_name = _('Порода')
        verbose_name_plural = _('Породы')

    def __str__(self):
        return '{}/{}'.format(self.pet_type, self.title)


class GenderSpec(models.Model):
    """
        Гендерные особенности 
    """
    GENDERS = (
        ('m', 'Самец'),
        ('f', 'Самка'),
    )

    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        blank=False, null=False,
        verbose_name=_('Порода'),
        related_name='gender_spec',
    )
    gender = models.CharField(
        _('Пол'),
        max_length=1,
        choices=GENDERS,
        blank=False, null=False,
        default='m',
    )
    body_length_min = models.PositiveIntegerField(
        _('Длина от, см'),
        blank=False, null=False,
        default=30
    )
    body_length_max = models.PositiveIntegerField(
        _('Длина до, см'),
        blank=False, null=False,
        default=50
    )
    body_height_min = models.PositiveIntegerField(
        _('Высота от, см'),
        blank=False, null=False,
        default=10
    )
    body_height_max = models.PositiveIntegerField(
        _('Высота до, см'),
        blank=False, null=False,
        default=30
    )
    body_weight_min = models.PositiveIntegerField(
        _('Вес от, кг'),
        blank=False, null=False,
        default=10
    )
    body_weight_max = models.PositiveIntegerField(
        _('Вес до, кг'),
        blank=False, null=False,
        default=30
    )

    class Meta:
        db_table = 'gender_spec'
        verbose_name = _('Гендерная особенность')
        verbose_name_plural = _('Гендерные особенности')

    def __str__(self):
        return '{}, {}'.format(self.breed, self.gender)


class EyeColor(models.Model):
    """
        Цвет глаз
    """
    COLORS = (
        ('grey', 'Серые'),
        ('green', 'Зелёные'),
        ('blue', 'Голубые'),
        ('brown', 'Коричневые'),
        ('black', 'Чёрные'),
        ('yellow', 'Жёлтые'),
    )

    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        blank=False, null=False,
        verbose_name=_('Порода'),
        related_name='eye_color',
    )
    color = models.CharField(
        _('Цвет'),
        max_length=30,
        choices=COLORS,
        blank=False, null=False,
        default='grey',
    )

    class Meta:
        db_table = 'eye_color'
        verbose_name = _('Цвет глаз')
        verbose_name_plural = _('Цвета глаз')

    def __str__(self):
        return '{}, {}'.format(self.breed, self.color)


class CoatColor(models.Model):
    """
        Окрас шерсти
    """
    COLORS = (
        ('grey', 'Серый'),
        ('white', 'Белый'),
        ('blue', 'Голубой'),
        ('brown', 'Коричневый'),
        ('black', 'Черный'),
    )

    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        blank=False, null=False,
        verbose_name=_('Порода'),
        related_name='coat_color',
    )
    color = models.CharField(
        _('Цвет'),
        max_length=30,
        choices=COLORS,
        blank=False, null=False,
        default='grey',
    )

    class Meta:
        db_table = 'coat_color'
        verbose_name = _('Окрас шерсти')
        verbose_name_plural = _('Окрасы шерсти')

    def __str__(self):
        return '{}, {}'.format(self.breed, self.color)
