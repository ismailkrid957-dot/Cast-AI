from pydantic import BaseModel, Field, field_validator
from typing import Dict


class RoleCreate(BaseModel):
    role_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    # Les clés sont les critères évalués et les valeurs leurs poids.
    criteria_weights: Dict[str, float] = Field(min_length=1)

    @field_validator("criteria_weights")
    @classmethod
    def validate_weights(cls, weights):
        if not weights:
            raise ValueError("Au moins un critère est requis.")
        if any(weight <= 0 for weight in weights.values()):
            raise ValueError("Tous les poids doivent être strictement positifs.")
        return weights


class CandidateCreate(BaseModel):
    candidate_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    role_id: str = Field(min_length=1)
    # Caractéristiques d'audition normalisées entre 0 et 1.
    features: Dict[str, float] = Field(default_factory=dict)

    @field_validator("features")
    @classmethod
    def validate_features(cls, features):
        if any(value < 0 or value > 1 for value in features.values()):
            raise ValueError("Chaque caractéristique doit être comprise entre 0 et 1.")
        return features


class Role(RoleCreate):
    pass


class Candidate(CandidateCreate):
    pass
