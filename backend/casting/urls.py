
from django.urls import path
from .views import ListeCreationScenarioView

urlpatterns = [
    path('scenarios/', ListeCreationScenarioView.as_view(), name='liste-creation-scenarios'),
]
