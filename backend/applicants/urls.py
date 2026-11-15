from django.urls import path
from .views import InscriptionCandidatView

urlpatterns = [
    path("inscription/", InscriptionCandidatView.as_view(), name="inscription-candidat"),
]
