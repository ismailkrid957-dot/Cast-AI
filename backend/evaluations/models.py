from django.db import models
from django.contrib.auth.models import User
from casting.models import Scenario, Role


class Audition(models.Model):
    STATUTS = [
        ("EN_ATTENTE", "En attente"),
        ("EN_COURS", "En cours de traitement"),
        ("TERMINEE", "Terminée"),
        ("ECHEC", "Échec"),
    ]

    candidat = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="auditions"
    )
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE, related_name="auditions"
    )
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="auditions"
    )
    video = models.FileField(upload_to="auditions/")
    statut = models.CharField(max_length=20, choices=STATUTS, default="EN_ATTENTE")
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidat.username} - {self.scenario.titre}"


class Evaluation(models.Model):
    audition = models.OneToOneField(
        Audition, on_delete=models.CASCADE, related_name="evaluation"
    )
    score_global = models.FloatField(null=True, blank=True)
    retour_evaluation = models.TextField(blank=True)
    date_evaluation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluation de {self.audition}"
