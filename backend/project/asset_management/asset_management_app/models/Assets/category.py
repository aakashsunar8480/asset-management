from django.db import models

from ..core import BaseModel
from asset_management_app.models.core.mixins import SoftDeleteModelMixin


class Category(BaseModel,SoftDeleteModelMixin):

    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=300)