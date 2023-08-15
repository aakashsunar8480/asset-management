from django.db import models

from ..core import BaseModel
from ..Employees import Employees
from .subcategory import SubCategory
from .vendors import Vendors
from asset_management_app.enums import AssetStatusEnum,WarrantyTypeEnum
from asset_management_app.models.core.mixins import SoftDeleteModelMixin


class Assets(BaseModel, SoftDeleteModelMixin):

    asset_id = models.CharField(max_length=200, unique=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    employees = models.ForeignKey(Employees,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[(choice.value, choice.name) for choice in AssetStatusEnum])
    primary_owner = models.CharField()
    purchase_date = models.DateField()
    vendor = models.ForeignKey(Vendors,on_delete=models.CASCADE)
    warranty_type = models.CharField(max_length=20, choices=[(choice.value, choice.name) for choice in WarrantyTypeEnum])
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()
