
from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):

    # Les différents types de comptes
    ROLES = [
        ('DIRECTEUR', 'Directeur de casting'),
        ('CANDIDAT', 'Candidat'),
    ]

    utilisateur = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profil'
    )

    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='CANDIDAT'
    )

    def __str__(self):
        return f"{self.utilisateur.username} - {self.role}"
