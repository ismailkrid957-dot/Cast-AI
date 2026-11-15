
from rest_framework import serializers
from .models import Audition


class AuditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audition
        fields = [
            'id',
            'candidat',
            'scenario',
            'video',
            'statut',
            'date_soumission',
        ]

        read_only_fields = [
            'id',
            'candidat',
            'statut',
            'date_soumission',
        ]
