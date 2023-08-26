"""BaseModel abstract model."""
import uuid

from django.db import models


class BaseModel(models.Model):
    """BaseModel abstract model."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID")

    class Meta:
        """Meta for BaseModel abstract model."""

        abstract = True
