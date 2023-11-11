"""AddSubCategory mutation."""
import graphene
from asset_management_app.models.Assets import SubCategory

from ...core.model_mutation import ModelMutation
from ..types.sub_category_type import SubCategoryType


class AddSubCategoryInput(graphene.InputObjectType):
    """AddSubCategory input type."""

    name = graphene.String(required=True, description="Name of the category")
    description = graphene.String(description="description of the category")


class AddSubCategory(ModelMutation):
    """AddSubCategory mutation."""

    category = graphene.Field(SubCategoryType)

    class Meta:
        """AddSubCategory meta."""

        model = SubCategory

    class Arguments:
        """AddSubCategory Arguments."""

        input = AddSubCategoryInput()
