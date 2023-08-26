"""AddCategory mutation."""
import graphene
from asset_management_app.models.Assets import Category

from ...core.model_mutation import ModelMutation
from ..types.category_type import CategoryType


class AddCategoryInput(graphene.InputObjectType):
    """AddCategory input type."""

    name = graphene.String(required=True, description="Name of the category")
    description = graphene.String(description="description of the category")


class AddCategory(ModelMutation):
    """AddCategory mutation."""

    category = graphene.Field(CategoryType)

    class Meta:
        """AddCategory meta."""

        model = Category

    class Arguments:
        """AddCategory Arguments."""

        input = AddCategoryInput()
