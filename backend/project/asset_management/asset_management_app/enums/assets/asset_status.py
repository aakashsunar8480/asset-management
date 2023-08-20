from enum import Enum


class AssetStatusEnum(Enum):

    AVAILABLE = "Available"
    IN_USE = "In Use"
    MAINTENANCE = "Maintenance"
    LOST = "Lost"
    RETIRED = "Retired"
