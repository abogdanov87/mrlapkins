from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin
from catalogs.models import (
    Breed, 
)


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
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
