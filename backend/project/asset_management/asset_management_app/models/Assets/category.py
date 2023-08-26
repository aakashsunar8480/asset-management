"""Category model."""
from asset_management_app.models.core.mixins import SoftDeleteModelMixin
from django.db import models

from ..core import BaseModel


class Category(BaseModel, SoftDeleteModelMixin):
    """Category model."""

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
