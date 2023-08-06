from django.db import models

from asset_management_app.enums import UserTypeEnum, UserStatusEnum
from asset_management_app.models.organization import Organization


class Users(models.Model):

    emp_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=[(choice.value, choice.name) for choice in UserTypeEnum])
    status = models.CharField(max_length=20, choices=[(choice.value, choice.name) for choice in UserStatusEnum])
