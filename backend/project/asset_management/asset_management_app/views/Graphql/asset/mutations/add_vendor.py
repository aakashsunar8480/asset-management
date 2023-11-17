"""AddCategory mutation."""
import graphene
from asset_management_app.models.Assets import Vendors

from ...core.model_mutation import ModelMutation
from ..types.vendors_type import VendorType


class AddVendorInput(graphene.InputObjectType):
    """AddCategory input type."""

    name = graphene.String(required=True, description="Name of the category")
    mobile = graphene.String(required=True, description="Contact of the category")
    email = graphene.String(required=True, description="Email of the category")
    description = graphene.String(description="description of the category")


class AddVendor(ModelMutation):
    """AddCategory mutation."""

    vendor = graphene.Field(VendorType)

    class Meta:
        """AddCategory meta."""

        model = Vendors

    class Arguments:
        """AddCategory Arguments."""

        input = AddVendorInput()
