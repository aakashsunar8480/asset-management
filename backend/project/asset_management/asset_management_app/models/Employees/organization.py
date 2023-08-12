from django.db import models

from ..core import BaseModel
from asset_management_app.models.core.mixins import SoftDeleteModelMixin


class Organization(BaseModel,SoftDeleteModelMixin):

    name = models.CharField(max_length=100)
