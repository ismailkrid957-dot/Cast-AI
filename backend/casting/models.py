
from django.db import models
from django.contrib.auth.models import User


class Scenario(models.Model):

    titre = models.CharField(max_length=200)

    description = models.TextField()

    cree_par = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='scenarios_crees'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
