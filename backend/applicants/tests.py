
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profil


class ProfilTests(TestCase):

    def test_creation_profil_candidat(self):
        utilisateur = User.objects.create_user(
            username="candidat_test",
            password="Test12345!"
        )

        profil = Profil.objects.get(utilisateur=utilisateur)

        self.assertEqual(profil.role, "CANDIDAT")
        self.assertEqual(profil.utilisateur, utilisateur)
