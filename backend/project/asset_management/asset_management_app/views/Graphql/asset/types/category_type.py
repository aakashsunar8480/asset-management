"""CategoryType."""
from asset_management_app.models.Assets import Category
from graphene_django.types import DjangoObjectType


class CategoryType(DjangoObjectType):
    """CategoryType return type."""

    class Meta:
        """CategoryType meta."""

        model = Category
