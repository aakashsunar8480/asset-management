from django.db import models

from ..core import BaseModel
from asset_management_app.models.core.mixins import SoftDeleteModelMixin


class Warranty(BaseModel,SoftDeleteModelMixin):

    warranty_type = models.CharField(max_length=100)
    duration = models.IntegerField()
