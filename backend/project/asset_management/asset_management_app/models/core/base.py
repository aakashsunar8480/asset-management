import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID")

    class Meta:
        abstract = True
