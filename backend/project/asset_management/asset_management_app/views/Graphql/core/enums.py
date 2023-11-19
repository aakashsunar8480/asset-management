"""Convert Python Enums into graphene Enums to be available for schema."""
import graphene

from asset_management_app.enums.employees import EmployTypeEnum, EmployStatusEnum

UserTypeEnum = graphene.Enum.from_enum(EmployTypeEnum)
UserStatusEnum = graphene.Enum.from_enum(EmployStatusEnum)