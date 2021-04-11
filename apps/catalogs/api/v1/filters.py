from django_filters import rest_framework as filters
from django.db.models import Q, CharField
from django.db.models.functions import Lower
from datetime import datetime
from catalogs.models import (
    Catalog, 
)


CharField.register_lookup(Lower)


class CatalogFilter(filters.FilterSet):
    class Meta:
        model = Catalog
        fields = ('active',)
