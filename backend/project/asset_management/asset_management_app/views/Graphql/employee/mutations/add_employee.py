"""AddEmployee mutation."""
from typing import Any

import graphene
from asset_management_app.models.Employees import Employees, Organization

from ...core.enums import UserStatusEnum, UserTypeEnum
from ...core.model_mutation import ModelMutation
from ..types.employee import EmployeeType


class AddEmployeeInput(graphene.InputObjectType):
    """AddEmployee input type."""

    name = graphene.String(required=True, description="Name of the Employee")
    emp_id = graphene.String(required=True, description="ID of the Employee")
    email = graphene.String(required=False, description="Email of the Employee")
    mobile = graphene.String(required=False, description="Mobile of the Employee")
    organization = graphene.String(
        required=False, description="Organization ID of the Employee"
    )
    user_type = graphene.Field(
        UserTypeEnum, required=True, description="User type of the Employee"
    )
    status = graphene.Field(
        UserStatusEnum, required=True, description="Status of the Employee"
    )


class AddEmployee(ModelMutation):
    """AddEmployee mutation."""

    employee = graphene.Field(EmployeeType)

    class Meta:
        """AddEmployee meta."""

        model = Employees

    class Arguments:
        """AddEmployee Arguments."""

        input = AddEmployeeInput()

    @classmethod
    def _clean_input(cls: Any, **data: dict) -> Any:
        """Input formatting and instance creation."""
        model = cls.get_model()
        data["organization"] = Organization.objects.get(id=data.get("organization"))
        instance = model(**data)
        return instance
