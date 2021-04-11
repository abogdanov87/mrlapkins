from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import (
    Catalog,
    User,
)


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    model = Catalog
    fields = [
        'pet_type',
        'breed',
        'short_description',
        'origin',
        'image',
        'allergenicity',
        'molt',
        'intelligence',
        'sociability',
        'need_for_care',
        'activity',
        'friendliness',
        'health',
        'active',
    ]
    list_display = ('pet_type', 'breed',)
    list_display_links = ('pet_type','breed')


class MyUserAdmin(UserAdmin):
    model = User
    list_display = (
        'id', 
        'username', 
        'last_name', 
        'first_name',
        'middle_name',
        'avatar',
    )
    list_display_links = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            _('Личные данные'),
            {
                'fields': (
                    'last_name',
                    'first_name',
                    'middle_name',
                    'avatar',
                ),
            },
        ),
        (
            _('Доступы'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
    )


admin.site.register(User, MyUserAdmin)
