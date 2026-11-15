
from rest_framework.permissions import BasePermission, SAFE_METHODS


class EstDirecteurOuLectureSeule(BasePermission):

    message = "Seul un directeur peut créer un scénario."

    def has_permission(self, request, view):

        # L'utilisateur doit être connecté
        if not request.user or not request.user.is_authenticated:
            return False

        # Tout utilisateur connecté peut consulter les scénarios
        if request.method in SAFE_METHODS:
            return True

        # Seul le directeur peut effectuer une écriture
        return (
            hasattr(request.user, 'profil')
            and request.user.profil.role == 'DIRECTEUR'
        )
