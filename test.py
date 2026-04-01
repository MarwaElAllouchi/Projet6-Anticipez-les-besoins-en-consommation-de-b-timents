import requests

url = "https://energy-service-123751721205.europe-west1.run.app/predict"

payload = {
    "parsed_json": {
    "PropertyGFATotal": 8000,
    "PropertyGFAParking": 5000,
    "LargestPropertyUseTypeGFA": 3000,
    "BuildingAge": 60,
    "SurfaceParEtage": 0,
    "SmallBuilding": 0,
    "MediumBuilding": 1,
    "TallBuilding": 0,
    "BuildingDensity": 0.26,
    "HasParking":1,
    "PrimaryPropertyType": "Hotel",
    "LargestPropertyUseType": "Hotel",
    "Neighborhood": "DOWNTOWN",
    "AgeCategory": "Vieux"
  }
}

response = requests.post(url, json=payload)
print(response.json())
