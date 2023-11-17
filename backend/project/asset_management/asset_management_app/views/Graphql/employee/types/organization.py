"""OrganizationType."""
from asset_management_app.models.Employees import Organization
from graphene_django.types import DjangoObjectType


class OrganizationType(DjangoObjectType):
    """OrganizationType return type."""

    class Meta:
        """OrganizationType meta."""

        model = Organization
