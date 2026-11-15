
from rest_framework import generics

from .models import Scenario
from .serializers import ScenarioSerializer
from .permissions import EstDirecteurOuLectureSeule


class ListeCreationScenarioView(generics.ListCreateAPIView):

    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
    permission_classes = [EstDirecteurOuLectureSeule]

    def perform_create(self, serializer):
        serializer.save(cree_par=self.request.user)
