"""SoftDeleteManager to override get_queryset."""
from typing import Any

from django.db import models


class SoftDeleteManager(models.Manager):
    """SoftDeleteManager to override get_queryset."""

    def get_queryset(self: Any) -> Any:
        """Override queryset to filter deleted records."""
        return super().get_queryset().filter(is_deleted=False)
