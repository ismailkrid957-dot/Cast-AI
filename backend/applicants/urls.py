from django.urls import path
from .views import InscriptionCandidatView

urlpatterns = [
    path("register/", InscriptionCandidatView.as_view(), name="inscription-candidat"),
]
