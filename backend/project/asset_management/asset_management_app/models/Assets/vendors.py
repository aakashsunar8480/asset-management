from django.db import models

from ..core import BaseModel
from asset_management_app.models.core.mixins import SoftDeleteModelMixin


class Vendors(BaseModel,SoftDeleteModelMixin):

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    description = models.CharField(max_length=200)
