"""Search result type."""
import graphene
from asset_management_app.models import (
    Assets,
    Category,
    Employees,
    Organization,
    SubCategory,
    Vendors,
)
from graphene_django import DjangoObjectType


class CategoryType(DjangoObjectType):
    """Category model type."""

    class Meta:
        """Meta."""

        model = Category


class SubCategoryType(DjangoObjectType):
    """SubCategory model type."""

    category = graphene.Field(CategoryType)

    class Meta:
        """Meta."""

        model = SubCategory


class OrganizationType(DjangoObjectType):
    """Organization model type."""

    class Meta:
        """Meta."""

        model = Organization


class EmployeeType(DjangoObjectType):
    """Employees model type."""

    organization = OrganizationType

    class Meta:
        """Meta."""

        model = Employees


class VendorType(DjangoObjectType):
    """Vendors model type."""

    class Meta:
        """Meta."""

        model = Vendors


class SearchResultType(DjangoObjectType):
    """Search result type."""

    subcategory = graphene.Field(SubCategoryType)
    employees = graphene.Field(EmployeeType)
    vendor = graphene.Field(VendorType)

    class Meta:
        """Meta."""

        model = Assets
        fields = "__all__"
