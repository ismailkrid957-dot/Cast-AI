from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from casting.models import Role
from casting.permissions import EstDirecteur, est_directeur
from .models import Audition, Evaluation
from .serializers import AuditionSerializer, EvaluationSerializer, ClassementSerializer


class DeposerAuditionView(generics.CreateAPIView):
    serializer_class = AuditionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        profil = getattr(self.request.user, "profil", None)
        if not profil or profil.role != "CANDIDAT":
            raise PermissionDenied("Seuls les candidats peuvent déposer une audition.")
        serializer.save(candidat=self.request.user)


class ListeAuditionsView(generics.ListAPIView):
    serializer_class = AuditionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Audition.objects.select_related("candidat", "scenario", "role")
        if est_directeur(user):
            return queryset.filter(scenario__cree_par=user)
        return queryset.filter(candidat=user)


class EvaluationAuditionView(APIView):
    permission_classes = [EstDirecteur]

    def get_audition(self, request, audition_id):
        audition = get_object_or_404(
            Audition.objects.select_related("scenario"), pk=audition_id
        )
        if audition.scenario.cree_par_id != request.user.id:
            raise PermissionDenied("Cette audition ne fait pas partie de vos castings.")
        return audition

    def get(self, request, audition_id):
        audition = self.get_audition(request, audition_id)
        evaluation = get_object_or_404(Evaluation, audition=audition)
        return Response(EvaluationSerializer(evaluation).data)

    def post(self, request, audition_id):
        audition = self.get_audition(request, audition_id)
        if Evaluation.objects.filter(audition=audition).exists():
            raise ValidationError("Cette audition possède déjà une évaluation. Utilisez PATCH.")
        serializer = EvaluationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        evaluation = serializer.save(audition=audition)
        audition.statut = "TERMINEE"
        audition.save(update_fields=["statut"])
        return Response(EvaluationSerializer(evaluation).data, status=status.HTTP_201_CREATED)

    def patch(self, request, audition_id):
        audition = self.get_audition(request, audition_id)
        evaluation = get_object_or_404(Evaluation, audition=audition)
        serializer = EvaluationSerializer(evaluation, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        evaluation = serializer.save()
        return Response(EvaluationSerializer(evaluation).data)


class Top15RoleView(generics.ListAPIView):
    serializer_class = ClassementSerializer
    permission_classes = [EstDirecteur]

    def get_queryset(self):
        role = get_object_or_404(Role.objects.select_related("scenario"), pk=self.kwargs["role_id"])
        if role.scenario.cree_par_id != self.request.user.id:
            raise PermissionDenied("Ce rôle ne fait pas partie de vos castings.")
        return (
            Audition.objects.filter(role=role, evaluation__score_global__isnull=False)
            .select_related("candidat", "evaluation")
            .order_by("-evaluation__score_global", "date_soumission")[:15]
        )
