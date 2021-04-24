from django_filters import rest_framework as filters
from django.db.models import Q, CharField
from django.db.models.functions import Lower
from datetime import datetime
from catalogs.models import (
    Breed, 
)


CharField.register_lookup(Lower)


class BreedFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', method='filter_title')

    class Meta:
        model = Breed
        fields = ('active', 'pet_type', 'title',)

    def filter_title(self, queryset, title, value):
        return queryset.filter(title__icontains=value)
