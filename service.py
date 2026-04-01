from __future__ import annotations
import bentoml
from bentoml.io import JSON
from pydantic import BaseModel, validator
import pandas as pd

# Import des enums
from enums import (
    PrimaryPropertyTypeEnum,
    LargestPropertyUseTypeEnum,
    NeighborhoodEnum,
    AgeCategoryEnum
)

# Définition de la classe d'entrée pour le service
class BuildingData(BaseModel):
    
    PropertyGFATotal: float
    PropertyGFAParking: float
    LargestPropertyUseTypeGFA: float
    BuildingAge: float
    SurfaceParEtage: float
    SmallBuilding: int
    MediumBuilding: int
    TallBuilding: int
    BuildingDensity: float
    HasParking: int
    PrimaryPropertyType: PrimaryPropertyTypeEnum
    LargestPropertyUseType: LargestPropertyUseTypeEnum
    Neighborhood: NeighborhoodEnum
    AgeCategory: AgeCategoryEnum

    # Exemple de normalisation si nécessaire
    @validator('Neighborhood', pre=True)
    def normalize_neighborhood(cls, v):
        if isinstance(v, str):
            return v.strip().upper()  # tout en majuscule pour Neighborhood
        return v

    @validator('PrimaryPropertyType', 'LargestPropertyUseType', 'AgeCategory', pre=True)
    def normalize_others(cls, v):
        if isinstance(v, str):
            return v.strip().title()  # première lettre en majuscule
        return v

# Charger le modèle BentoML enregistré

@bentoml.service( resources={"cpu": "2"},
    traffic={"timeout": 10}, )


class EnergyService:

    def __init__(self):
        self.model = bentoml.sklearn.load_model("best_energy_model:latest")
        print(type (self.model))
        # Afficher la pipeline pour vérification
        print("Pipeline chargée :", self.model)
        print(self.model.named_steps['preprocessor'].transformers)
    @bentoml.api
    async def predict(self, parsed_json: BuildingData):
        """
        Prend un JSON conforme à BuildingData et retourne la prédiction
        """
        # Convertir les données en DataFrame pour le modèle
        df = pd.DataFrame([parsed_json.dict()])
        # Faire la prédiction via le runner
        prediction = self.model.predict(df)
        return {"prediction": prediction.tolist()}
