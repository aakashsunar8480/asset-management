"""SubCategory model."""
from asset_management_app.models.core.mixins import SoftDeleteModelMixin
from django.db import models

from ..core import BaseModel


class SubCategory(BaseModel, SoftDeleteModelMixin):
    """SubCategory model."""

    category = models.ForeignKey(
        "asset_management_app.Category", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=300)
    model = models.CharField(max_length=200, unique=True)
    host_name = models.CharField(max_length=200, unique=True)
