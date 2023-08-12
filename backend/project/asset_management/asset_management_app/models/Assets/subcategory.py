from django.db import models
from .category import Category
from ..core import BaseModel
from asset_management_app.models.core.mixins import SoftDeleteModelMixin


class SubCategory(BaseModel,SoftDeleteModelMixin):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=300)
    model = models.CharField(max_length=200, unique=True)
    host_name = models.CharField(max_length=200,unique=True)


