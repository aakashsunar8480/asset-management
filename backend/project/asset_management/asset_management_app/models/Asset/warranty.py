from django.db import models


class Warranty(models.Model):

    warranty_type = models.CharField(max_length=100)
    duration = models.IntegerField()
