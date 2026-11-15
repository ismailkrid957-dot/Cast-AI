from rest_framework import serializers
from .models import Scenario, Role


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ["id", "titre", "description", "cree_par", "date_creation"]
        read_only_fields = ["id", "cree_par", "date_creation"]


class RoleSerializer(serializers.ModelSerializer):
    scenario_titre = serializers.CharField(source="scenario.titre", read_only=True)

    class Meta:
        model = Role
        fields = [
            "id", "scenario", "scenario_titre", "titre", "description",
            "criteres_evaluation", "date_creation"
        ]
        read_only_fields = ["id", "scenario_titre", "date_creation"]

    def validate_scenario(self, scenario):
        request = self.context["request"]
        if scenario.cree_par_id != request.user.id:
            raise serializers.ValidationError(
                "Vous ne pouvez ajouter un rôle qu'à votre propre casting."
            )
        return scenario
