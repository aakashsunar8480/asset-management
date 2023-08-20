from asset_management_app.models.core.mixins import SoftDeleteModelMixin
from django.db import models

from ..core import BaseModel


class Organization(BaseModel, SoftDeleteModelMixin):

    name = models.CharField(max_length=100)
