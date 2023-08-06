from django.db import models
from ..Users import Users
from .subcategory import SubCategory
from .vendors import Vendors
from .warranty import Warranty
from asset_management_app.enums import AssetStatusEnum


class Assets(models.Model):

    asset_id = models.CharField(max_length=200, unique=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    warranty = models.ForeignKey(Warranty,on_delete=models.CASCADE)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[(choice.value, choice.name) for choice in AssetStatusEnum])
    primary_owner = models.CharField()
    purchase_date = models.DateField()
    vendor = models.ForeignKey(Vendors,on_delete=models.CASCADE)
