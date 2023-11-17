"""SubCategoryType."""
from asset_management_app.models.Assets import SubCategory
from graphene_django.types import DjangoObjectType


class SubCategoryType(DjangoObjectType):
    """SubCategoryType return type."""

    class Meta:
        """SubCategoryType meta."""

        model = SubCategory
