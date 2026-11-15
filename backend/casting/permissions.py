from rest_framework.permissions import BasePermission, SAFE_METHODS


def est_directeur(user):
    return (
        user.is_authenticated
        and hasattr(user, "profil")
        and user.profil.role == "DIRECTEUR"
    )


class EstDirecteurOuLectureSeule(BasePermission):
    message = "Seul un directeur peut créer ou modifier un casting."

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True
        return est_directeur(request.user)


class EstDirecteur(BasePermission):
    message = "Cette action est réservée aux directeurs de casting."

    def has_permission(self, request, view):
        return est_directeur(request.user)
