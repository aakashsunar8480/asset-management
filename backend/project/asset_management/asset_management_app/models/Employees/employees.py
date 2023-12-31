"""Employees model."""
from asset_management_app.enums.employees import EmployStatusEnum, EmployTypeEnum
from asset_management_app.models.core.mixins import SoftDeleteModelMixin
from django.db import models

from ..core import BaseModel


class Employees(BaseModel, SoftDeleteModelMixin):
    """Employees model."""

    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    organization = models.ForeignKey(
        "asset_management_app.Organization", on_delete=models.CASCADE
    )
    user_type = models.CharField(
        max_length=50,
        choices=[(choice.value, choice.name) for choice in EmployTypeEnum],
    )
    status = models.CharField(
        max_length=50,
        choices=[(choice.value, choice.name) for choice in EmployStatusEnum],
    )
