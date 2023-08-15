from django.db import models

from asset_management_app.enums import EmployStatusEnum, EmployTypeEnum
from ..core import BaseModel
from asset_management_app.models.Employees.organization import Organization
from asset_management_app.models.core.mixins import SoftDeleteModelMixin


class Employees(BaseModel, SoftDeleteModelMixin):
    emp_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=[(choice.value, choice.name) for choice in EmployTypeEnum])
    status = models.CharField(max_length=20, choices=[(choice.value, choice.name) for choice in EmployStatusEnum])
