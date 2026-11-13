from app.models import Candidate, Role
from app.scoring import score_candidate, build_shortlist


def sample_role():
    return Role(
        role_id="R1",
        title="Rôle dramatique",
        criteria_weights={
            "articulation": 0.5,
            "vocal_clarity": 0.3,
            "gesture_clarity": 0.2,
        },
    )


def test_role_specific_weighted_score():
    role = sample_role()
    candidate = Candidate(
        candidate_id="C1",
        name="Candidate 1",
        role_id="R1",
        features={
            "articulation": 1.0,
            "vocal_clarity": 0.5,
            "gesture_clarity": 0.0,
        },
    )
    result = score_candidate(candidate, role)
    assert result["score"] == 0.65
    assert result["status"] == "scored"


def test_missing_features_are_flagged():
    role = sample_role()
    candidate = Candidate(
        candidate_id="C2",
        name="Candidate 2",
        role_id="R1",
        features={"articulation": 0.8},
    )
    result = score_candidate(candidate, role)
    assert result["missing_criteria"] == ["vocal_clarity", "gesture_clarity"]
    assert result["status"] == "needs_review"


def test_shortlist_is_role_specific_and_limited():
    role = sample_role()
    candidates = [
        Candidate(
            candidate_id=f"C{i:02}",
            name=f"Candidate {i}",
            role_id="R1",
            features={
                "articulation": i / 20,
                "vocal_clarity": i / 20,
                "gesture_clarity": i / 20,
            },
        )
        for i in range(1, 21)
    ]
    candidates.append(
        Candidate(
            candidate_id="OTHER",
            name="Other role",
            role_id="R2",
            features={"articulation": 1, "vocal_clarity": 1, "gesture_clarity": 1},
        )
    )

    result = build_shortlist(candidates, role, limit=15)
    assert len(result) == 15
    assert result[0]["candidate_id"] == "C20"
    assert all(item["role_id"] == "R1" for item in result)
    assert all(item["final_human_review_required"] for item in result)
