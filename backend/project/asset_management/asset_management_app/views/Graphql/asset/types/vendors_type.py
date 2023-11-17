"""VendorType."""
from asset_management_app.models.Assets import Vendors
from graphene_django.types import DjangoObjectType


class VendorType(DjangoObjectType):
    """VendorType return type."""

    class Meta:
        """VendorType meta."""

        model = Vendors
