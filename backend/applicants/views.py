from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import InscriptionCandidatSerializer


class InscriptionCandidatView(generics.CreateAPIView):
    serializer_class = InscriptionCandidatSerializer
    permission_classes = [AllowAny]
