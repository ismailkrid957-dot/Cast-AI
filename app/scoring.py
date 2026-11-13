from app.models import Candidate, Role


def score_candidate(candidate: Candidate, role: Role) -> dict:
    """Score pondéré selon la grille propre au rôle.

    Les critères absents sont exclus du calcul et signalés. En production,
    une candidature incomplète devrait être mise en vérification plutôt que
    pénalisée silencieusement.
    """
    applicable = {
        key: weight
        for key, weight in role.criteria_weights.items()
        if key in candidate.features
    }
    missing = [
        key for key in role.criteria_weights
        if key not in candidate.features
    ]

    if not applicable:
        return {
            "score": None,
            "criteria_used": [],
            "missing_criteria": missing,
            "status": "needs_review",
        }

    total_weight = sum(applicable.values())
    weighted_sum = sum(
        candidate.features[key] * weight
        for key, weight in applicable.items()
    )

    return {
        "score": round(weighted_sum / total_weight, 4),
        "criteria_used": list(applicable.keys()),
        "missing_criteria": missing,
        "status": "needs_review" if missing else "scored",
    }


def build_shortlist(
    candidates: list[Candidate],
    role: Role,
    limit: int = 15,
) -> list[dict]:
    if limit < 1:
        raise ValueError("La limite doit être supérieure ou égale à 1.")

    results = []
    for candidate in candidates:
        if candidate.role_id != role.role_id:
            continue
        evaluation = score_candidate(candidate, role)
        if evaluation["score"] is None:
            continue
        results.append({
            "candidate_id": candidate.candidate_id,
            "name": candidate.name,
            "role_id": candidate.role_id,
            **evaluation,
            "final_human_review_required": True,
        })

    # En cas d'égalité, l'identifiant rend le résultat déterministe.
    results.sort(key=lambda item: (-item["score"], item["candidate_id"]))
    return results[:limit]
