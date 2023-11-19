"""EmployeeType."""
from asset_management_app.models.Employees import Employees
from graphene_django.types import DjangoObjectType


class EmployeeType(DjangoObjectType):
    """EmployeeType return type."""

    class Meta:
        """EmployeeType meta."""

        model = Employees
