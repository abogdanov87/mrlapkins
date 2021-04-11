from django_filters import rest_framework as filters
from django.db.models import Q, CharField
from django.db.models.functions import Lower
from datetime import datetime
from catalogs.models import (
    Breed, 
)


CharField.register_lookup(Lower)


class BreedFilter(filters.FilterSet):
    class Meta:
        model = Breed
        fields = ('active',)
