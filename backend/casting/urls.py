from django.urls import path
from .views import ListeCreationScenarioView, ListeCreationRoleView

urlpatterns = [
    path("scenarios/", ListeCreationScenarioView.as_view(), name="liste-creation-scenarios"),
    path("roles/", ListeCreationRoleView.as_view(), name="liste-creation-roles"),
]
