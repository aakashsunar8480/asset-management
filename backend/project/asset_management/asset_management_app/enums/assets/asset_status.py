"""Asset status enum."""
from enum import Enum


class AssetStatusEnum(Enum):
    """Asset status enum."""

    AVAILABLE = "Available"
    IN_USE = "In Use"
    MAINTENANCE = "Maintenance"
    LOST = "Lost"
    RETIRED = "Retired"
