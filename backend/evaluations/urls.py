from django.urls import path
from .views import DeposerAuditionView, ListeAuditionsView, EvaluationAuditionView, Top15RoleView

urlpatterns = [
    path("auditions/", ListeAuditionsView.as_view(), name="liste-auditions"),
    path("auditions/deposer/", DeposerAuditionView.as_view(), name="deposer-audition"),
    path("auditions/<int:audition_id>/evaluation/", EvaluationAuditionView.as_view(), name="evaluation-audition"),
    path("roles/<int:role_id>/top15/", Top15RoleView.as_view(), name="top15-role"),
]
