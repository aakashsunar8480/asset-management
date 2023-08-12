from django.utils import timezone

from django.db import models

from asset_management_app.models.core.managers import SoftDeleteManager


class SoftDeleteModelMixin(models.Model):
    is_deleted = models.BooleanField(default=False, help_text="Flag representing if object is set to be deleted.")
    deleted_at = models.DateTimeField(null=True, blank=True, help_text="Timestamp at which this object was deleted.")

    objects = SoftDeleteManager()

    class Meta:
        abstract = True

    def delete(self, *args,**kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(*args,**kwargs)

    def restore(self,*args,**kwargs):
        self.is_deleted = False
        self.deleted_at = None
        self.save(*args, **kwargs)
