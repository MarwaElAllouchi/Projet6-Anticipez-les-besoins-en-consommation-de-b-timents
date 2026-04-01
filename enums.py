from enum import Enum
from pydantic import BaseModel, validator
from typing import Optional

# --- Enums ---
class PrimaryPropertyTypeEnum(str, Enum):
    Hotel = "Hotel"
    Other = "Other"
    MixedUseProperty = "Mixed Use Property"
    University = "University"
    SmallAndMidSizedOffice = "Small- and Mid-Sized Office"
    SelfStorageFacility = "Self-Storage Facility"
    Warehouse = "Warehouse"
    K12School = "K-12 School"
    LargeOffice = "Large Office"
    SeniorCareCommunity = "Senior Care Community"
    MedicalOffice = "Medical Office"
    RetailStore = "Retail Store"
    Hospital = "Hospital"
    ResidenceHall = "Residence Hall"
    WorshipFacility = "Worship Facility"
    SupermarketGroceryStore = "Supermarket / Grocery Store"
    DistributionCenter = "Distribution Center"
    Laboratory = "Laboratory"
    RefrigeratedWarehouse = "Refrigerated Warehouse"
    Restaurant = "Restaurant"
    LowRiseMultifamily = "Low-Rise Multifamily"


class LargestPropertyUseTypeEnum(str, Enum):
    Hotel = "Hotel"
    OtherEntertainmentPublicAssembly = "Other - Entertainment/Public Assembly"
    FitnessCenterHealthClubGym = "Fitness Center/Health Club/Gym"
    SocialMeetingHall = "Social/Meeting Hall"
    Courthouse = "Courthouse"
    Other = "Other"
    CollegeUniversity = "College/University"
    AutomobileDealership = "Automobile Dealership"
    Office = "Office"
    SelfStorageFacility = "Self-Storage Facility"
    NonRefrigeratedWarehouse = "Non-Refrigerated Warehouse"
    K12School = "K-12 School"
    OtherMall = "Other - Mall"
    SeniorCareCommunity = "Senior Care Community"
    MedicalOffice = "Medical Office"
    RetailStore = "Retail Store"
    HospitalGeneralMedicalSurgical = "Hospital (General Medical & Surgical)"
    Museum = "Museum"
    OtherLodgingResidential = "Other - Lodging/Residential"
    ResidenceHallDormitory = "Residence Hall/Dormitory"
    # … ajoute toutes les autres valeurs ici


class NeighborhoodEnum(str, Enum):
    DOWNTOWN = "DOWNTOWN"
    NORTHEAST = "NORTHEAST"
    EAST = "EAST"
    LAKE_UNION = "LAKE UNION"
    GREATER_DUWAMISH = "GREATER DUWAMISH"
    BALLARD = "BALLARD"
    NORTHWEST = "NORTHWEST"
    MAGNOLIA_QUEEN_ANNE = "MAGNOLIA / QUEEN ANNE"
    CENTRAL = "CENTRAL"
    SOUTHWEST = "SOUTHWEST"
    SOUTHEAST = "SOUTHEAST"
    NORTH = "NORTH"


class AgeCategoryEnum(str, Enum):
    Neuf = "Neuf"
    Moyen = "Moyen"
    Vieux = "Vieux"


# --- Pydantic model ---
class BuildingData(BaseModel):

    PropertyGFATotal: float
    PropertyGFAParking: float
    LargestPropertyUseTypeGFA: float
    BuildingAge: int
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


    # --- Validators pour uniformiser la casse ---
    @validator('PrimaryPropertyType', pre=True)
    def normalize_primary_property_type(cls, v):
        if isinstance(v, str):
            return v.title().strip()
        return v

    @validator('LargestPropertyUseType', pre=True)
    def normalize_largest_property_use_type(cls, v):
        if isinstance(v, str):
            return v.title().strip()
        return v

    @validator('Neighborhood', pre=True)
    def normalize_neighborhood(cls, v):
        if isinstance(v, str):
            return v.upper().strip()
        return v

    @validator('AgeCategory', pre=True)
    def normalize_age_category(cls, v):
        if isinstance(v, str):
            return v.title().strip()
        return v
