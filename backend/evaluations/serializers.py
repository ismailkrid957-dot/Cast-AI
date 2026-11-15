from rest_framework import serializers
from .models import Audition, Evaluation


class AuditionSerializer(serializers.ModelSerializer):
    candidat_username = serializers.CharField(source="candidat.username", read_only=True)
    role_titre = serializers.CharField(source="role.titre", read_only=True)

    class Meta:
        model = Audition
        fields = [
            "id", "candidat", "candidat_username", "scenario", "role",
            "role_titre", "video", "statut", "date_soumission"
        ]
        read_only_fields = [
            "id", "candidat", "candidat_username", "statut", "date_soumission"
        ]
        extra_kwargs = {
            "role": {"required": True, "allow_null": False},
        }

    def validate(self, attrs):
        role = attrs.get("role")
        scenario = attrs.get("scenario")
        if role and scenario and role.scenario_id != scenario.id:
            raise serializers.ValidationError(
                {"role": "Ce rôle n'appartient pas au casting sélectionné."}
            )
        return attrs

    def validate_video(self, video):
        allowed = (".mp4", ".mov", ".avi", ".webm", ".m4v")
        name = video.name.lower()
        if not name.endswith(allowed):
            raise serializers.ValidationError(
                "Format vidéo accepté : mp4, mov, avi, webm ou m4v."
            )
        return video


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = [
            "id", "audition", "score_global", "retour_evaluation",
            "date_evaluation"
        ]
        read_only_fields = ["id", "audition", "date_evaluation"]
        extra_kwargs = {
            "score_global": {"required": True, "allow_null": False},
        }

    def validate_score_global(self, score):
        if score is None or not 0 <= score <= 100:
            raise serializers.ValidationError("La note doit être comprise entre 0 et 100.")
        return score


class ClassementSerializer(serializers.ModelSerializer):
    candidat = serializers.CharField(source="candidat.username", read_only=True)
    score = serializers.FloatField(source="evaluation.score_global", read_only=True)
    commentaire = serializers.CharField(
        source="evaluation.retour_evaluation", read_only=True
    )

    class Meta:
        model = Audition
        fields = ["id", "candidat", "role", "video", "score", "commentaire"]
