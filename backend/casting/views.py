from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Scenario, Role
from .serializers import ScenarioSerializer, RoleSerializer
from .permissions import EstDirecteurOuLectureSeule


class ListeCreationScenarioView(generics.ListCreateAPIView):
    queryset = Scenario.objects.select_related("cree_par").all()
    serializer_class = ScenarioSerializer
    permission_classes = [EstDirecteurOuLectureSeule]

    def perform_create(self, serializer):
        serializer.save(cree_par=self.request.user)


class ListeCreationRoleView(generics.ListCreateAPIView):
    queryset = Role.objects.select_related("scenario").all()
    serializer_class = RoleSerializer
    permission_classes = [EstDirecteurOuLectureSeule]
