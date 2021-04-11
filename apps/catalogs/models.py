import os
from django.db import models
from django.contrib.auth.models import AbstractUser
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


class User(AbstractUser):
    """
        CustomUser
    """

    first_name = models.CharField(
        _('Имя'),
        max_length=30,
        blank=True, null=True,
    )
    last_name = models.CharField(
        _('Фамилия'),
        max_length=30,
        blank=True, null=True,
    )
    middle_name = models.CharField(
        _('Отчество'),
        max_length=30,
        blank=True, null=True,
    )
    email = models.EmailField(
        _('Адрес электронной почты'),
        blank=True, null=True,
    )
    avatar = ThumbnailerImageField(
        _('Аватарка'),
        upload_to ='avatars/',
        blank=True, null=True,
        resize_source=dict(size=(128, 128), sharpen=True),
    )
    password_change_date = models.DateTimeField(
        _('Дата изменения пароля'),
        default=timezone.datetime(year=1970, month=1, day=1),
    )

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


class Catalog(models.Model):
    """
        Каталог 
    """
    pet_type = models.CharField(
        _('Вид питомца'),
        max_length=30,
        choices=PET_TYPES,
        blank=False, null=False,
        default='cat'
    )
    breed = models.CharField(
        _('Порода'),
        max_length=255,
        blank=False, null=False,
        default='',
    )
    short_description = models.CharField(
        _('Краткое описание'),
        max_length=2000,
        blank=False, null=False,
        default='',
    )
    origin = models.CharField(
        _('Происхождение'),
        max_length=2000,
        blank=False, null=False,
        default='',
    )
    image = ThumbnailerImageField(
        _('Логотип'),
        upload_to ='badges/',
        blank=True, null=True,
        resize_source=dict(size=(128, 128), sharpen=True),
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
        db_table = 'catalog'
        verbose_name = _('Каталог')
        verbose_name_plural = _('Каталоги')

    def __str__(self):
        return '{}/{}'.format(self.pet_type, self.breed)
