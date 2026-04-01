🏢 Anticipez les besoins en consommation de bâtiments

📌 Contexte

Ce projet a été réalisé dans le cadre d’une étude de prédiction de la consommation énergétique des bâtiments non résidentiels.

L’objectif est d’aider à anticiper les besoins énergétiques des bâtiments afin de contribuer à une meilleure gestion de l’énergie et à la réduction des émissions de carbone.

Le cas d’usage s’appuie sur des données de bâtiments de la ville de Seattle.

🎯 Objectifs

Explorer et comprendre les facteurs influençant la consommation énergétique
Préparer un jeu de données exploitable pour la modélisation
Concevoir de nouvelles variables pertinentes (feature engineering)
Comparer plusieurs modèles de régression
Sélectionner le meilleur modèle de prédiction
Emballer le modèle dans une pipeline reproductible
Exposer le modèle via une API avec BentoML

📊 Données utilisées

Le dataset contient des informations sur les bâtiments, notamment :

type de bâtiment
année de construction
surface totale
surface de parking
type principal d’usage
quartier
nombre d’étages
consommation énergétique
Variable cible

La variable cible prédite est :

SiteEnergyUseWN(kBtu)
consommation énergétique totale du bâtiment

🧹 Préparation et nettoyage des données

La première étape du projet a consisté à :

charger le dataset des bâtiments
filtrer les bâtiments non résidentiels
conserver uniquement les bâtiments conformes
sélectionner les colonnes les plus pertinentes
Nettoyage

Le nettoyage a inclus :

suppression des valeurs incohérentes
traitement des valeurs manquantes
détection et suppression des outliers avec la méthode IQR
visualisation avant/après nettoyage
Principaux constats de l’EDA

L’analyse exploratoire a montré que :

la surface totale du bâtiment influence fortement la consommation énergétique
le type de bâtiment est un facteur explicatif important
certaines valeurs extrêmes peuvent perturber les performances des modèles

🏗️ Feature Engineering

Afin d’améliorer les performances du modèle, plusieurs variables ont été créées :

BuildingAge : âge du bâtiment
SurfaceParEtage : surface moyenne par étage
SmallBuilding / MediumBuilding / TallBuilding : catégorisation selon le nombre d’étages
BuildingDensity : densité du bâtiment
HasParking : indicateur de présence d’un parking
AgeCategory : catégorie d’âge du bâtiment

Des variables additionnelles ont aussi été exploitées :

LargestPropertyUseType
Neighborhood
LargestPropertyUseTypeGFA
PropertyGFAParking
Prétraitements
encodage des variables catégorielles
standardisation des variables numériques
séparation train / test
suppression des variables peu utiles ou redondantes

🤖 Modélisation

Plusieurs modèles de régression ont été entraînés et comparés :

Régression linéaire
Ridge
Lasso
Random Forest
XGBoost
SVR
Méthodes d’évaluation

Les modèles ont été comparés avec :

R²
MAE
RMSE
Cross-validation
GridSearchCV pour l’optimisation des hyperparamètres

L’objectif était de sélectionner le modèle offrant le meilleur compromis entre performance et généralisation.

🧠 Pipeline de prédiction

Le modèle final n’a pas été sauvegardé seul.

Une pipeline sklearn complète a été construite pour intégrer :

le prétraitement numérique avec StandardScaler
l’encodage catégoriel avec OneHotEncoder
le modèle final sélectionné

Cette approche garantit que les nouvelles données envoyées au modèle subissent exactement les mêmes transformations que les données d’entraînement.

💾 Sauvegarde du modèle

Le pipeline final a été sauvegardé avec BentoML :

saved_model = bentoml.sklearn.save_model("best_energy_model", pipeline)

Le modèle sauvegardé inclut :

préprocessing
encodage
scaling
modèle entraîné

🚀 Mise en service avec BentoML

Une API de prédiction a été développée avec BentoML afin de rendre le modèle exploitable.

Fonctionnement du service

Le service :

charge le modèle best_energy_model:latest
reçoit un JSON décrivant un bâtiment
valide les données d’entrée
convertit les données en DataFrame pandas
renvoie une prédiction de consommation énergétique
Service principal

Le fichier service.py expose une classe EnergyService avec une API predict.

✅ Validation des entrées

Pour sécuriser l’API, les entrées sont validées avec Pydantic et des Enum métier.

Champs d’entrée

L’API attend notamment :

PropertyGFATotal
PropertyGFAParking
LargestPropertyUseTypeGFA
BuildingAge
SurfaceParEtage
SmallBuilding
MediumBuilding
TallBuilding
BuildingDensity
HasParking
PrimaryPropertyType
LargestPropertyUseType
Neighborhood
AgeCategory
Contrôles appliqués
validation du type des champs
restriction des catégories possibles via Enum
normalisation automatique de certaines valeurs textuelles

Cela améliore la robustesse du service et limite les erreurs de format.

📦 Packaging du service

Le déploiement est configuré avec bentofile.yaml.

Ce fichier décrit :

le point d’entrée du service
les fichiers inclus
les dépendances Python
le modèle BentoML embarqué
Dépendances principales
bentoml
pandas
numpy
scikit-learn
fastapi
uvicorn
pydantic

🗂️ Structure du projet

Exemple de structure :

.
├── service.py
├── enums.py
├── bentofile.yaml
├── requirements.txt
├── notebooks/
│   ├── eda_preprocessing.ipynb
│   └── modeling_bentoml.ipynb
└── data/
    └── 2016_Building_Energy_Benchmarking.csv
▶️ Lancer le service
1. Entraîner et sauvegarder le modèle

Exécuter le notebook de modélisation pour générer :

best_energy_model
2. Servir l’API BentoML
bentoml serve service.py:EnergyService
3. Appeler l’API

Exemple de payload JSON :

{
  "PropertyGFATotal": 120000,
  "PropertyGFAParking": 10000,
  "LargestPropertyUseTypeGFA": 85000,
  "BuildingAge": 35,
  "SurfaceParEtage": 8000,
  "SmallBuilding": 0,
  "MediumBuilding": 1,
  "TallBuilding": 0,
  "BuildingDensity": 12.0,
  "HasParking": 1,
  "PrimaryPropertyType": "Hotel",
  "LargestPropertyUseType": "Hotel",
  "Neighborhood": "DOWNTOWN",
  "AgeCategory": "Moyen"
}

Réponse attendue :

{
  "prediction": [1234567.89]
}
📈 Résultats et valeur du projet

Ce projet démontre la capacité à :

mener une analyse exploratoire complète
nettoyer et préparer des données réelles
concevoir des features métier pertinentes
comparer plusieurs modèles de machine learning
construire une pipeline de prédiction robuste
packager et versionner un modèle avec BentoML
exposer un modèle via une API exploitable

🔍 Compétences mobilisées

Data analysis
Data cleaning
Feature engineering
Machine learning
Model evaluation
API serving
BentoML
Pydantic
scikit-learn

🚀 Perspectives d’amélioration4

suivi de drift des données
ajout de monitoring modèle
tests automatiques de l’API
conteneurisation complète du service
déploiement cloud
ajout d’une seconde cible, par exemple les émissions de CO₂

👩‍💻 Auteur

Projet réalisé par Marwa El Allouchi
Data Engineer / Data & ML Projects – OpenClassrooms