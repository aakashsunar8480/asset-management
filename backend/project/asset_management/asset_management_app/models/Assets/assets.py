"""Asset model."""
from asset_management_app.enums.assets import AssetStatusEnum, WarrantyTypeEnum
from asset_management_app.models.core.mixins import SoftDeleteModelMixin
from django.db import models

from ..core import BaseModel


class Assets(BaseModel, SoftDeleteModelMixin):
    """Asset model."""

    asset_id = models.CharField(max_length=200, unique=True)
    subcategory = models.ForeignKey(
        "asset_management_app.SubCategory", on_delete=models.CASCADE
    )
    employees = models.ForeignKey(
        "asset_management_app.Employees", on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=[(choice.value, choice.name) for choice in AssetStatusEnum],
    )
    primary_owner = models.CharField()
    purchase_date = models.DateField()
    vendor = models.ForeignKey("asset_management_app.Vendors", on_delete=models.CASCADE)
    warranty_type = models.CharField(
        max_length=20,
        choices=[(choice.value, choice.name) for choice in WarrantyTypeEnum],
    )
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()
