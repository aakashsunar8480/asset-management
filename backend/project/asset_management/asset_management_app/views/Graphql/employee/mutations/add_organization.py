"""AddOrganization mutation."""
import graphene
from asset_management_app.models.Employees import Organization

from ...core.model_mutation import ModelMutation
from ..types.organization import OrganizationType


class AddOrganizationInput(graphene.InputObjectType):
    """AddOrganization input type."""

    name = graphene.String(required=True, description="Name of the organization")


class AddOrganization(ModelMutation):
    """AddOrganization mutation."""

    organization = graphene.Field(OrganizationType)

    class Meta:
        """AddOrganization meta."""

        model = Organization

    class Arguments:
        """AddOrganization Arguments."""

        input = AddOrganizationInput()
