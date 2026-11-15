
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Scenario, Role


class ScenarioModelTests(TestCase):

    def setUp(self):
        self.directeur = User.objects.create_user(
            username="directeur",
            password="Test12345!"
        )

    def test_creation_scenario(self):
        scenario = Scenario.objects.create(
            titre="Casting publicité",
            description="Recherche de comédiens",
            cree_par=self.directeur
        )

        self.assertEqual(scenario.titre, "Casting publicité")
        self.assertEqual(scenario.cree_par, self.directeur)

    def test_creation_role(self):
        scenario = Scenario.objects.create(
            titre="Film",
            cree_par=self.directeur
        )

        role = Role.objects.create(
            scenario=scenario,
            titre="Acteur principal",
            description="Rôle principal"
        )

        self.assertEqual(role.titre, "Acteur principal")
        self.assertEqual(role.scenario, scenario)

