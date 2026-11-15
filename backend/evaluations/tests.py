
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from casting.models import Scenario, Role
from .models import Audition, Evaluation


class AuditionEvaluationTests(TestCase):

    def setUp(self):
        self.directeur = User.objects.create_user(
            username="directeur",
            password="Test12345!"
        )
        self.candidat = User.objects.create_user(
            username="candidat",
            password="Test12345!"
        )

        self.scenario = Scenario.objects.create(
            titre="Casting film",
            cree_par=self.directeur
        )

        self.role = Role.objects.create(
            scenario=self.scenario,
            titre="Acteur principal"
        )

    def test_creation_audition(self):
        video = SimpleUploadedFile(
            "audition.mp4",
            b"fichier video de test",
            content_type="video/mp4"
        )

        audition = Audition.objects.create(
            candidat=self.candidat,
            scenario=self.scenario,
            role=self.role,
            video=video
        )

        self.assertEqual(audition.statut, "EN_ATTENTE")
        self.assertEqual(audition.role, self.role)

    def test_creation_evaluation(self):
        video = SimpleUploadedFile(
            "audition.mp4",
            b"fichier video de test",
            content_type="video/mp4"
        )

        audition = Audition.objects.create(
            candidat=self.candidat,
            scenario=self.scenario,
            role=self.role,
            video=video
        )

        evaluation = Evaluation.objects.create(
            audition=audition,
            score_global=85,
            retour_evaluation="Très bonne prestation"
        )

        self.assertEqual(evaluation.score_global, 85)
        self.assertEqual(evaluation.audition, audition)


from rest_framework.test import APIClient
from django.urls import reverse



class PermissionsEvaluationTests(TestCase):

    def test_candidat_peut_deposer_audition(self):
        directeur = User.objects.create_user(username="directeur")
        candidat = User.objects.create_user(username="candidat")

        scenario = Scenario.objects.create(
            titre="Film",
            cree_par=directeur
        )
        role = Role.objects.create(
            scenario=scenario,
            titre="Acteur"
        )

        client = APIClient()
        client.force_authenticate(user=candidat)

        response = client.post(
            reverse("deposer-audition"),
            {
                "scenario": scenario.id,
                "role": role.id,
                "video": SimpleUploadedFile(
                    "audition.mp4",
                    b"video test",
                    content_type="video/mp4"
                )
            },
            format="multipart"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Audition.objects.count(), 1)


    def test_candidat_ne_peut_pas_evaluer(self):
        directeur = User.objects.create_user(username="directeur")
        directeur.profil.role = "DIRECTEUR"
        directeur.profil.save()

        candidat = User.objects.create_user(username="candidat")
        scenario = Scenario.objects.create(titre="Film", cree_par=directeur)
        role = Role.objects.create(scenario=scenario, titre="Acteur")

        audition = Audition.objects.create(
            candidat=candidat,
            scenario=scenario,
            role=role,
            video=SimpleUploadedFile("video.mp4", b"test")
        )

        client = APIClient()
        client.force_authenticate(user=candidat)

        url = reverse("evaluation-audition", kwargs={"audition_id": audition.id})
        response = client.post(url, {"score_global": 85})

        self.assertEqual(response.status_code, 403)

    def test_directeur_ne_peut_pas_evaluer_casting_autrui(self):
        directeur1 = User.objects.create_user(username="directeur1")
        directeur1.profil.role = "DIRECTEUR"
        directeur1.profil.save()

        directeur2 = User.objects.create_user(username="directeur2")
        directeur2.profil.role = "DIRECTEUR"
        directeur2.profil.save()

        candidat = User.objects.create_user(username="candidat")
        scenario = Scenario.objects.create(titre="Film", cree_par=directeur1)
        role = Role.objects.create(scenario=scenario, titre="Acteur")

        audition = Audition.objects.create(
            candidat=candidat,
            scenario=scenario,
            role=role,
            video=SimpleUploadedFile("video.mp4", b"test")
        )

        client = APIClient()
        client.force_authenticate(user=directeur2)

        url = reverse("evaluation-audition", kwargs={"audition_id": audition.id})
        response = client.post(url, {"score_global": 90})

        self.assertEqual(response.status_code, 403)
