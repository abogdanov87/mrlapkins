from rest_framework import serializers
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin
from feedbacks.models import (
    Feedback,
)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
            'breed',
            'title',
            'description',
            'created',
            'user',
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
