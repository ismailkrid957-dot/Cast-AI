from fastapi import FastAPI, HTTPException, Query
from app.models import Role, RoleCreate, Candidate, CandidateCreate
from app.scoring import build_shortlist
from app.feature_extractor import extract_audition_features

app = FastAPI(
    title="CastingIA",
    description=(
        "Présélection assistée par IA avec une grille de critères propre "
        "à chaque rôle. L'évaluation finale reste humaine."
    ),
    version="0.2.0",
)

roles: dict[str, Role] = {}
candidates: dict[str, Candidate] = {}


@app.get("/")
def home():
    return {
        "project": "CastingIA",
        "status": "prototype",
        "principle": "L'IA présélectionne ; l'équipe de casting évalue les finalistes.",
    }


@app.post("/roles", response_model=Role)
def create_role(role_data: RoleCreate):
    if role_data.role_id in roles:
        raise HTTPException(status_code=409, detail="Ce rôle existe déjà.")
    role = Role(**role_data.model_dump())
    roles[role.role_id] = role
    return role


@app.get("/roles", response_model=list[Role])
def list_roles():
    return list(roles.values())


@app.post("/candidates", response_model=Candidate)
def add_candidate(candidate_data: CandidateCreate):
    if candidate_data.candidate_id in candidates:
        raise HTTPException(status_code=409, detail="Cette candidature existe déjà.")
    if candidate_data.role_id not in roles:
        raise HTTPException(status_code=404, detail="Rôle introuvable. Créez d'abord le rôle.")
    candidate = Candidate(**candidate_data.model_dump())
    candidates[candidate.candidate_id] = candidate
    return candidate


@app.get("/candidates", response_model=list[Candidate])
def list_candidates(role_id: str | None = None):
    result = list(candidates.values())
    if role_id:
        result = [candidate for candidate in result if candidate.role_id == role_id]
    return result


@app.get("/roles/{role_id}/shortlist")
def get_shortlist(
    role_id: str,
    limit: int = Query(default=15, ge=1, le=500),
):
    role = roles.get(role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Rôle introuvable.")

    role_candidates = [
        candidate for candidate in candidates.values()
        if candidate.role_id == role_id
    ]
    shortlist = build_shortlist(role_candidates, role, limit)

    return {
        "role_id": role_id,
        "role_title": role.title,
        "applications_received": len(role_candidates),
        "shortlist_limit": limit,
        "shortlist_count": len(shortlist),
        "shortlist": shortlist,
        "notice": (
            "Présélection indicative selon la grille de ce rôle. "
            "L'équipe de casting doit évaluer les profils et prendre la décision finale."
        ),
    }


@app.get("/feature-extraction/status")
def feature_extraction_status():
    return extract_audition_features("demo")
