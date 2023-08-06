from django.db import models
from .category import Category


class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=300)
    model = models.CharField(max_length=200, unique=True)
    host_name = models.CharField(max_length=200,unique=True)


