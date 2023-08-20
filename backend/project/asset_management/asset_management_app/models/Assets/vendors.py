from asset_management_app.models.core.mixins import SoftDeleteModelMixin
from django.db import models

from ..core import BaseModel


class Vendors(BaseModel, SoftDeleteModelMixin):

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    description = models.CharField(max_length=200)
