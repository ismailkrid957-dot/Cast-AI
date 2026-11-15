
from rest_framework import serializers
from .models import Scenario


class ScenarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scenario
        fields = [
            'id',
            'titre',
            'description',
            'cree_par',
            'date_creation',
        ]

        read_only_fields = [
            'id',
            'cree_par',
            'date_creation',
        ]
