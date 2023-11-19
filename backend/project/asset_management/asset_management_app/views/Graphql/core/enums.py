"""Convert Python Enums into graphene Enums to be available for schema."""
import graphene
from asset_management_app.enums.employees import EmployStatusEnum, EmployTypeEnum

UserTypeEnum = graphene.Enum.from_enum(EmployTypeEnum)
UserStatusEnum = graphene.Enum.from_enum(EmployStatusEnum)
