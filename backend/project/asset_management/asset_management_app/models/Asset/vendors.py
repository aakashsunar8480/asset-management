from django.db import models


class Vendors(models.Model):

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    description = models.CharField(max_length=200)
