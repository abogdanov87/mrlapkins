from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin
from catalogs.models import (
    Catalog, 
    User, 
)


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = (
            'id',
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
        )

    def validate(self, data):
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'last_name',
            'first_name',
            'middle_name',
            'avatar',
        )

    def validate(self, data):
        return data
