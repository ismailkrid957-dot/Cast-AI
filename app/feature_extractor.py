"""Point d'extension pour les futurs modules d'analyse vidéo et audio.

Cette version ne contient pas de modèle IA entraîné. Elle ne déduit pas les
émotions, la personnalité, la sincérité ou le talent à partir de l'apparence,
du visage, de la voix ou des mouvements.

Les futures caractéristiques devront décrire des éléments observables et
pertinents pour la prestation, être validées pour chaque rôle et ne pas
remplacer l'évaluation finale de l'équipe de casting.
"""


def extract_audition_features(video_path: str) -> dict:
    """Emplacement réservé à l'intégration future des modèles."""
    return {
        "status": "not_implemented",
        "message": (
            "L'extraction automatique des caractéristiques vidéo/audio "
            "n'est pas encore intégrée. Fournir des caractéristiques de "
            "démonstration ou connecter un modèle validé."
        ),
        "video_received": bool(video_path),
        "features": {},
    }
