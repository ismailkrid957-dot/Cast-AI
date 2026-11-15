from django.db import models
from django.contrib.auth.models import User


class Scenario(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cree_par = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="scenarios_crees"
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Role(models.Model):
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE, related_name="roles"
    )
    titre = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    criteres_evaluation = models.TextField(
        blank=True,
        help_text="Critères utilisés par le directeur pour évaluer les auditions."
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["titre"]
        unique_together = [("scenario", "titre")]

    def __str__(self):
        return f"{self.titre} — {self.scenario.titre}"
