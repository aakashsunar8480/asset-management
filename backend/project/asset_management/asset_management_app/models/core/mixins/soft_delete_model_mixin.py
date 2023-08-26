"""SoftDeleteModelMixin to override delete."""
from typing import Any

from asset_management_app.models.core.managers import SoftDeleteManager
from django.db import models
from django.utils import timezone


class SoftDeleteModelMixin(models.Model):
    """SoftDeleteModelMixin to override delete."""

    is_deleted = models.BooleanField(
        default=False, help_text="Flag representing if object is set to be deleted."
    )
    deleted_at = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp at which this object was deleted."
    )

    objects = SoftDeleteManager()

    class Meta:
        """SoftDeleteModelMixin meta."""

        abstract = True

    def delete(self: Any, *args: list, **kwargs: dict) -> None:
        """Delete method override."""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(*args, **kwargs)

    def restore(self: Any, *args: list, **kwargs: dict) -> None:
        """Restore method override."""
        self.is_deleted = False
        self.deleted_at = None
        self.save(*args, **kwargs)
